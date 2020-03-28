from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	gluOrtho2D(-200.0,200.0,-200.0,200.0)
	glPointSize(3.0)

def Sign(x):
	if x<0:
		return -1
	elif x==0:
		return 0
	else:
		return 1

def setPixel(xcoordinate,ycoordinate):

    glBegin(GL_POINTS)
    glVertex2i(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

def lineBressenham(x1,y1,x2,y2):
	x=x1
	y=y1
	dx=abs(x2-x1)
	dy=abs(y2-y1)
	s1=Sign(x2-x1)
	s2=Sign(y2-y1)
	Interchange=0

	if dy>dx:
		Temp=dx
		dx=dy
		dy=Temp
		Interchange=1
	else:
		Interchange=0

	e=(2*dy)-dx

	for i in range(1,dx+1):
		setPixel(x,y)
		while e>0:
			if Interchange==1:
				x=x+s1
			else:
				y=y+s2
			e=e-(2*dx)
		if Interchange==1:
			y=y+s2
		else:
			x=x+s1
		e=e+(2*dy)

def intake():
	global x1,y1,x2,y2
	x1,y1,x2,y2=map(int,input("Coordinate:").split())

def disp():
	glClear(GL_COLOR_BUFFER_BIT)
	lineBressenham(x1, y1, x2, y2)


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(50,50)
	glutCreateWindow("bressenham line")
	intake()
	glutDisplayFunc(disp)
	init()
	glutMainLoop()
	

if __name__ == "__main__":
	main()
