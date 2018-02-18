from OpenGL.GL import *
from OpenGL.GLu import *
from OpenGL.GLut import *
import numpy as np
from math import *
def face():
    # Circle face
    glColor(0,1,0)
    glBegin(GL_POLYGON_BIT)
    r = 0.255
    x0= 0.0
    y0 = 0.6
    for theta in np.arange(0,2*pi,0.001):
        x = x0 + r * cos(theta)
        y = y0 + r * sin(theta)
        glVertex2d(x,y)
    glEnd()
    glFlush()
    #Circle Right eye
    glColor(1,1,1)
    glBegin(GL_POLYGON)
    r = 0.02
    x0 = 0.15
    y0 = 0.65
    for theta in np.arange(0, 2 * pi, 0.001):
        x = x0 + r * cos(theta)
        y = y0 + r * sin(theta)
        glVertex2d(x, y)
    glEnd()
    glFlush()
    #Circle left eye
    glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    r = 0.02
    x0 = -0.15
    y0 = 0.65
    for theta in np.arange(0, 2 * pi, 0.001):
        x = x0 + r * cos(theta)
        y = y0 + r * sin(theta)
        glVertex2d(x, y)
    glEnd()
    glFlush()
def knec():
    glColor3d(0.3,0.4,1.0)
    glBegin(GL_POLYGON)
    glVertex2d(0.07,0.3)
    glVertex2d(0.07,0.35)
    glVertex2d(-0.07, 0.35)
    glVertex2d(-0.07, 0.3)
    glEnd()
def body():
    glColor3d(0.3,0.4,1.0)
    glBegin(GL_POLYGON)
    glVertex2d(0.3, 0.3)
    glVertex2d(0.3, -0.3)
    glVertex2d(-0.3, -0.3)
    glVertex2d(-0.3, 0.3)
    glEnd()
def legs():
    #right leg

    glColor3d(1,0.8,0.6)
    glBegin(GL_POLYGON)
    glVertex2d(0.15, -0.3)
    glVertex2d(0.25, -0.3)
    glVertex2d(0.25, -0.7)
    glVertex2d(0.15, -0.7)
    glEnd()
    #left leg
    glColor3d(1, 0.8, 0.6)
    glBegin(GL_POLYGON)
    glVertex2d(-0.15, -0.3)
    glVertex2d(-0.15, -0.7)
    glVertex2d(-0.25, -0.7)
    glVertex2d(-0.25, -0.3)
    glEnd()
def hande():
    #right hand

    glColor3d(0.8, 0.9, 1.0)
    glBegin(GL_POLYGON)
    glVertex2d(0.3, 0.3)
    glVertex2d(0.7, 0.0)
    glVertex2d(0.65, -0.1)
    glVertex2d(0.3, 0.2)
    glEnd()
    #left hand
    glColor3d(1, 0.8, 0.6)
    glBegin(GL_POLYGON)
    glVertex2d(-0.3, 0.3)
    glVertex2d(-0.7, 0.0)
    glVertex2d(-0.65, -0.1)
    glVertex2d(-0.3, 0.2)
    glEnd()
def dol():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    face()
    body()
    knec()
    hande()
    legs()
    glFlush()
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"frist Program")
glutDisplayFunc(draw1)
glutMainLoop()












