from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	gluOrtho2D(-200.0,200.0,-200.0,200.0)
	glPointSize(3.0)

def ROUND(a):
	return int(a+0.5)

def drawDDA(x1,y1,x2,y2):
	x,y=x1,y1
	dx=x2-x1
	dy=y2-y1
	steps=abs(dx) if abs(dx)>abs(dy) else abs(dy)
	Xinc=dx/float(steps)
	Yinc=dy/float(steps)
	for i in range(steps):
                       glBegin(GL_POINTS)
                       x += Xinc
                       y += Yinc
                       glVertex2f(x, y)
                       glEnd()

	glFlush()

def intake():
	global x1,y1,x2,y2
	x1,y1,x2,y2=map(int,input("Coordinate:").split())

def disp():
	glClear(GL_COLOR_BUFFER_BIT)
	drawDDA(x1, y1, x2, y2)

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(50,50)
	glutCreateWindow("dda line")
	intake()
	glutDisplayFunc(disp)
	init()
	glutMainLoop()
	

if __name__ == "__main__":
	main()

	