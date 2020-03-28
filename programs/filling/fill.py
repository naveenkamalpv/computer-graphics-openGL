from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys

sys.setrecursionlimit(1500000000)
pi = 3.14


def init():
    glClearColor(0, 0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, 640, 0, 480)


def floodfill(x, y, oldcolor, newcolor):
    currentColor = glReadPixels(x, y, 1.0, 1.0, GL_RGB, GL_FLOAT)
    if (currentColor != oldcolor).any():
        return
    glColor3f(newcolor[0], newcolor[1], newcolor[2])
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()
    glFlush()
    floodfill(x + 2, y, oldcolor, newcolor)
    floodfill(x + 2, y + 2, oldcolor, newcolor)
    floodfill(x + 2, y - 2, oldcolor, newcolor)
    floodfill(x - 2, y, oldcolor, newcolor)
    floodfill(x - 2, y + 2, oldcolor, newcolor)
    floodfill(x - 2, y - 2, oldcolor, newcolor)
    floodfill(x, y + 2, oldcolor, newcolor)
    floodfill(x, y - 2, oldcolor, newcolor)


def boundaryfill(x, y, fillColor, boundaryColor):
    color = glReadPixels(x, y, 1.0, 1.0, GL_RGB, GL_FLOAT)
    if (color != boundaryColor).any() and (color != fillColor).any():
        glColor3f(fillColor[0], fillColor[1], fillColor[2])
        glBegin(GL_POINTS)
        glVertex2i(x, y)
        glEnd()
        glFlush()
        boundaryfill(x + 2, y, fillColor, boundaryColor)
        boundaryfill(x - 2, y, fillColor, boundaryColor)
        boundaryfill(x, y + 2, fillColor, boundaryColor)
        boundaryfill(x, y - 2, fillColor, boundaryColor)


def mouse(button, state, x, y):
    y = 480 - y
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            if choice == 1:
                newcolor = [1, 1, 1]
                oldcolor = glReadPixels(x, y, 1.0, 1.0, GL_RGB, GL_FLOAT)
                floodfill(x, y, oldcolor, newcolor)
            elif choice == 2:
                boundaryColor = [1, 0, 0]
                color = [0, 0, 0]
                boundaryfill(x, y, color, boundaryColor)


def plot():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(5.0)
    glPointSize(3.0)
    glBegin(GL_LINE_LOOP)
    glColor3f(1, 0, 0)
    glVertex2i(150, 100)
    glVertex2i(250, 250)
    glVertex2i(350, 100)
    glVertex2i(250, 150)
    glEnd()
    for i in range(361):
        m = float(50 * (math.cos(i * pi / 180.0))) + 100
        n = float(50 * (math.sin(i * pi / 180.0))) + 100
        glBegin(GL_POINTS)
        glColor3f(1, 0, 0)
        glVertex2f(m, n)
        glEnd()

    glFlush()


def read():
    global choice
    choice = int(input("1.Flood Fill\n2.Boundary Fill\n Enter your Choice : "))


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(200, 200)
    glutCreateWindow('Polygon Flood fill')
    read()
    glutDisplayFunc(plot)
    glutMouseFunc(mouse)
    init()
    glutMainLoop()


if __name__ == "__main__":
    main()
