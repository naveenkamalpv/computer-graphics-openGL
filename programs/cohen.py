from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from ddaline_import import drawDDA 
import sys
import math

INSIDE = 0 	#0000
LEFT = 1   	#0001
RIGHT = 2  	#0010
BOTTOM = 4 	#0100
TOP = 8    	#1000

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-200.0, 200.0, -200.0, 200.0)
    glPointSize(5.0)

def plot():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)

    # draw a line
    glBegin(GL_LINES)
    glVertex2i(-200, 0)
    glVertex2i(200, 0)
    glVertex2i(0, -200)
    glVertex2i(0, 200)
    glEnd()
    #  draw rectangle
    glBegin(GL_LINE_LOOP)
    glVertex2f(x_min, y_min)
    glVertex2f(x_max, y_min)
    glVertex2f(x_max, y_max)
    glVertex2f(x_min, y_max)
    glEnd()
    glFlush()
    inputLines()


def inputWindow():
    global x_min, y_min, x_max, y_max
    x_min, y_min, x_max, y_max = map(int, input(
        'Enter the window coordinates in the order of x_min y_min x_max y_max : ').split())

def inputLines():
    choice = True
    while (choice == True):
        choice = False
        x1, y1, x2, y2 = map(int, input('Enter the line coordinates x1, y1, x2, y2 : ').split())
        cohen(x1, y1, x2, y2)
        choice = input("To Enter another Line,press y : ")
        if choice == 'y' or choice == 'Y': choice = True


def regionCode(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code


def cohen(x1, y1, x2, y2):
    code1 = regionCode(x1, y1)
    code2 = regionCode(x2, y2)
    accept = False
    while True:
        if code1 == 0 and code2 == 0:  # inside the window
            accept = True
            break
        elif (code1 & code2) != 0:   # outside window
            break
        else:
            x = 0.0
            y = 0.0
            dx = x2 - x1
            dy = y2 - y1
            if dx != 0:  # for handling divide by 0
                m = dy / dx

            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                y = y_max
                if dx == 0:  # when slope of line is infinity or undefined
                    x = x1
                else:
                    x = x1 + (y_max - y1) / m
            elif code_out & BOTTOM:
                y = y_min
                if dx == 0:  # when slope of line is infinity or undefined
                    x = x1
                else:
                    x = x1 + (y_min - y1) / m
            elif code_out & RIGHT:
                x = x_max
                y = y1 + m * (x_max - x1)
            elif code_out & LEFT:
                x = x_min
                y = y1 + m * (x_min - x1)

            if code_out == code1:
                x1 = x
                y1 = y
                code1 = regionCode(x1, y1)
            else:
                x2 = x
                y2 = y
                code2 = regionCode(x2, y2)

    if accept:
        drawDDA(x1, y1, x2, y2)
    else:
        print("Line is rejected! ")


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow('Cohen Line clipping')
    inputWindow()
    glutDisplayFunc(plot)
    init()
    glutMainLoop()


if __name__ == "__main__":
    main()
