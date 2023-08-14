import time
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np


#------------------------------LINE ALGORITHM----------------------------------------------------------
def findZone(x1,y1,x2,y2):
   dx = x2 - x1
   dy = y2 - y1
   zone = ''
   if abs(dx) > abs(dy):
       if (dx >= 0) and (dy >= 0):
           zone = '0'
       elif (dx >= 0) and (dy <= 0):
           zone = '7'
       elif (dx <= 0) and (dy >= 0):
           zone = '3'
       else:
           zone = '4'
   else:
       if (dx >= 0) and (dy >= 0):
           zone = '1'
       elif (dx >= 0) and (dy <= 0):
           zone = '6'
       elif (dx <= 0) and (dy >= 0):
           zone = '2'
       else:
           zone = '5'
   return zone

def originalToZero(x,y,zone):
   if zone == '0':
       return x,y
   elif zone == '1':
       return y,x
   elif zone == '2':
       return -y,x
   elif zone == '3':
       return -x,y
   elif zone == '4':
       return -x,-y
   elif zone == '5':
       return -y,-x
   elif zone == '6':
       return -y,x
   else:
       return x,-y


def zeroToOriginal(x,y,zone):
   if zone == '0':
       glVertex2f(x,y)
   elif zone == '1':
       glVertex2f(y,x)
   elif zone == '2':
       glVertex2f(-y,x)
   elif zone == '3':
       glVertex2f(-x,y)
   elif zone == '4':
       glVertex2f(-x,-y)
   elif zone == '5':
       glVertex2f(-y,-x)
   elif zone == '6':
       glVertex2f(y,-x)
   else:
       glVertex2f(x,-y)

def midPoint(x1,y1,x2,y2):
   zone = findZone(x1,y1,x2,y2)
   x1,y1 = originalToZero(x1,y1,zone)
   x2,y2 = originalToZero(x2,y2,zone)
   dx = x2 - x1
   dy = y2 - y1
   d = (2*dy) - dx
   east = 2*dy
   northeast = 2*(dy-dx)
   x = x1
   y = y1
   while x <= x2:
       zeroToOriginal(x,y,zone)
       x += 1
       if d > 0:
           d += northeast
           y += 1
       else:
           d += east
#--------------------------------------------------------------------------------------------------------

#---------------------------------CIRCLE ALGORITHM-------------------------------------------------------
def all_points(x,y,xOG,yOG):

    glVertex2f(x+xOG, y+yOG)
    glVertex2f(y+xOG, x+yOG)
    #glVertex2f(y+xOG, (x*-1)+yOG)
    #glVertex2f(x+xOG, (y*-1)+yOG)
    #glVertex2f((x*-1)+xOG, (y*-1)+yOG)
    #glVertex2f((y*-1)+xOG,(x*-1)+yOG)
    glVertex2f((y*-1)+xOG, x+yOG)
    glVertex2f((x*-1)+xOG, y+yOG)

def drawCircle(radius,xOG,yOG):
    d = 1 - radius
    x = 0
    y = radius
    all_points(x,y,xOG,yOG)
    while x < y:
        if d < 0:
            d = d + (2*x) + 3
            x += 1
        else:
            d = d + (2*x) - (2*y) + 5
            x += 1
            y -= 1
        all_points(x,y,xOG,yOG)

def all_points2(x, y, xOG, yOG):

    glVertex2f(x + xOG, y + yOG)
    glVertex2f(y + xOG, x + yOG)
    glVertex2f(y+xOG, (x*-1)+yOG)
    glVertex2f(x+xOG, (y*-1)+yOG)
    glVertex2f((x*-1)+xOG, (y*-1)+yOG)
    glVertex2f((y*-1)+xOG,(x*-1)+yOG)
    glVertex2f((y * -1) + xOG, x + yOG)
    glVertex2f((x * -1) + xOG, y + yOG)

def drawCircle2(radius, xOG, yOG):
    d = 1 - radius
    x = 0
    y = radius
    all_points(x, y, xOG, yOG)
    while x < y:
        if d < 0:
            d = d + (2 * x) + 3
            x += 1
        else:
            d = d + (2 * x) - (2 * y) + 5
            x += 1
            y -= 1
        all_points2(x, y, xOG, yOG)

def all_points3(x,y,xOG,yOG):

    #glVertex2f(x+xOG, y+yOG)
    #glVertex2f(y+xOG, x+yOG)
    glVertex2f(y+xOG, (x*-1)+yOG)
    glVertex2f(x+xOG, (y*-1)+yOG)
    glVertex2f((x*-1)+xOG, (y*-1)+yOG)
    glVertex2f((y*-1)+xOG,(x*-1)+yOG)
    #glVertex2f((y*-1)+xOG, x+yOG)
    #glVertex2f((x*-1)+xOG, y+yOG)

def drawCircle3(radius,xOG,yOG):
    d = 1 - radius
    x = 0
    y = radius
    all_points3(x,y,xOG,yOG)
    while x < y:
        if d < 0:
            d = d + (2*x) + 3
            x += 1
        else:
            d = d + (2*x) - (2*y) + 5
            x += 1
            y -= 1
        all_points3(x,y,xOG,yOG)
#----------------------------------------------------------------------------------------------------------


#-----------------------------------------SCENERY--------------------------------------------------------
def scenery ():
    glPointSize(2)
    glBegin(GL_POINTS)

    glColor3f(0.0, 0.9, 0.0)
    midPoint(0, 0, 500, 0) #light green meadow beginning line

    #midPoint(0, 0, 0, 200) #
    midPoint(0, 200, 500, 200) #light green meadow finishing line
    #midPoint(500, 0, 500, 200)
    x1 = 0
    y1 = 1
    x2 = 500
    y2 = 1
    while y1 != 200:
        midPoint(x1, y1, x2, y2)
        y1 += 1
        y2 += 1

    glColor3f(0.686, 0.933, 0.933)
    midPoint(0, 200, 500, 200)
    midPoint(0, 500, 500, 500)
    #midPoint(500, 200, 500, 500)
    x1 = 0
    y1 = 201
    x2 = 500
    y2 = 201
    while y1 != 500:
        midPoint(x1, y1, x2, y2)
        y1 += 1
        y2 += 1

    big_radius = 180
    big_x = 350
    big_y = 200
    glColor3f(0.0, 0.3, 0.0)
    drawCircle(big_radius, big_x, big_y)
    big_radius -= 1

    while big_radius != 0:

        drawCircle(big_radius, big_x, big_y)
        big_radius -= 1

    big_radius2 = 150
    big_x2 = 100
    big_y2 = 200
    glColor3f(0.0, 0.3, 0.0)
    drawCircle(big_radius2, big_x2, big_y2)
    big_radius2 -= 1

    while big_radius2 != 0:
        drawCircle(big_radius2, big_x2, big_y2)
        big_radius2 -= 1

    mid_radius = 130
    mid_x = 300
    mid_y = 200
    glColor3f(0.0, 0.5, 0.0)
    drawCircle(mid_radius, mid_x, mid_y)
    mid_radius -= 1

    while mid_radius != 0:
        drawCircle(mid_radius, mid_x, mid_y)
        mid_radius -= 1

    small_radius = 110
    small_x = 430
    small_y = 200
    glColor3f(0.0, 0.7, 0.0)
    drawCircle(small_radius, small_x, small_y)
    small_radius -= 1

    while small_radius != 0:
        drawCircle(small_radius, small_x, small_y)
        small_radius -= 1

    small_radius2 = 110
    small_x2 = 100
    small_y2 = 200
    glColor3f(0.0, 0.7, 0.0)
    drawCircle(small_radius2, small_x2, small_y2)
    small_radius2 -= 1

    while small_radius2 != 0:
        drawCircle(small_radius2, small_x2, small_y2)
        small_radius2 -= 1





    glEnd()

#------------------------------------------------------------------------