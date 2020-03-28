from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import numpy
import sys

sys.setrecursionlimit(1500000000)
pi = 3.14


def init():
    glClearColor(0, 0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, 640, 0, 480)


def boundaryfill(x, y, fillColor, boundaryColor):
    color = glReadPixels(x,y,1.0,1.0,GL_RGB,GL_FLOAT)
    if ((color != boundaryColor).any() and (color != fillColor).any()):
        glColor3f(fillColor[0],fillColor[1],fillColor[2])
        glBegin(GL_POINTS)
        glVertex2i(x, y)
        glEnd()
        glFlush()
        boundaryfill(x + 2, y, fillColor, boundaryColor)
        boundaryfill(x - 2, y, fillColor, boundaryColor)
        boundaryfill(x, y + 2, fillColor, boundaryColor)
        boundaryfill(x, y - 2, fillColor, boundaryColor)


def mouse(button, state, x, y):
    y = 480-y
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            boundaryColor = [1, 1, 0]
            color = [0, 0, 0]
            boundaryfill(x, y, color, boundaryColor)


def plot():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(2)
    glPointSize(3.0)
    glColor3f(1,1,0)
    '''
    glColor3f(10, 0, 10)
    glBegin(GL_LINE_LOOP)
    glVertex2i(00, 00)
    glVertex2i(500, 00)
    glVertex2i(500, 400)
    glVertex2i(0, 400)
    glEnd()'''
    glBegin(GL_LINE_LOOP)
    glVertex2i(150, 100)
    glVertex2i(300, 300)
    glVertex2i(450, 100)
    glVertex2i(250, 150)
    glEnd()
    for i in range(361):
        m = float(50 * (math.cos(i * pi / 180.0))) + 100
        n = float(50 * (math.sin(i * pi / 180.0))) + 100
        glBegin(GL_POINTS)
        glVertex2f(m, n)
        glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640,480)
    glutInitWindowPosition(200,200)
    glutCreateWindow('Polygon Boundary fill')
    glutDisplayFunc(plot)
    glutMouseFunc(mouse)
    init()
    glutMainLoop()


if __name__ == "__main__":
    main()
