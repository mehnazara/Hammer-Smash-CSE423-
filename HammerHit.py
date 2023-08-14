import time
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import math
from Scenery import scenery, findZone, originalToZero, zeroToOriginal, midPoint, all_points,all_points2, drawCircle, drawCircle2,drawCircle3,all_points3



#-------------------------------------Scale----------------------------------
def scale(factor):
   glPointSize(2)
   glBegin(GL_POINTS)

   glColor3f(0.545, 0.271, 0.0745)
   midPoint(100,50,180,50)
   midPoint(100,50,100,450) #width
   midPoint(180,50,180,450) #width
   midPoint(100,450,180,450)
   x1 = 100
   y1 = 51
   x2 = 180
   y2 = 51

   glColor3f(1.0, 0.9, 0.0)
   while y1 != 450:

       midPoint(x1,y1,x2,y2)
       y1 += 1
       y2 += 1

   glColor3f(0.27, 0.07, 0.0)
   midPoint(125, 75, 155, 75)
   midPoint(155, 75, 155, 420)
   midPoint(125, 75, 125, 420)
   midPoint(125, 420, 155, 420)

   temp_y = 75
   while temp_y < 421:
       if temp_y <= 250:
           glColor3f(0.727, 0.522, 0.176)
           midPoint(125, temp_y, 155, temp_y)
           temp_y += 1
       elif 250 < temp_y <= 350:
           glColor3f(0.627, 0.322, 0.176)
           midPoint(125, temp_y, 155, temp_y)
           temp_y += 1
       elif 350 < temp_y <= 420:
           glColor3f(0.27, 0.07, 0.0)
           midPoint(125, temp_y, 155, temp_y)
           temp_y += 1
   # lowest scale
   glColor3f(0.627, 0.322, 0.176)
   midPoint(170, 150, 190, 150)
   midPoint(170, 151, 190, 151)

   # middle scale
   midPoint(170, 250, 190, 250)
   midPoint(170, 251, 190, 251)

   # highest scale
   midPoint(170, 350, 190, 350)
   midPoint(170, 351, 190, 351)

   bar(bar_y1)

   glColor3f(0.627, 0.322, 0.176)
   midPoint(80, 50, 200, 50)
   midPoint(80, 50, 80, 75)
   midPoint(200, 50, 200, 75)
   midPoint(80, 75, 200, 75)
   x1 = 80
   y1 = 51
   x2 = 200
   y2 = 51
   while y1 != 75:
       midPoint(x1, y1, x2, y2)
       y1 += 1
       y2 += 1

   glColor3f(1.0, 1.0, 1.0)
   center_x = 140
   center_y = 76
   radius = 47*factor  #scaling
   drawCircle(radius,center_x,center_y)
   radius -= 1
   while radius > 0.5:
       glColor3f(1.0, 0.894, 0.7098)
       drawCircle(radius, center_x, center_y)
       radius -= 1

   glEnd()
#-----------------------------------------------------------------------

#--------------------------------BAR---------------------------------------------
def bar(y1):
    glColor3f(0.627, 0.122, 0.0)
    count = 5
    while count != 0:
        midPoint(90, y1, 190, y1)
        y1 += 1
        count -= 1
    if (y1 == 456):
        glColor3f(1.0,0.5,0.0)

        midPoint(90,470,100,460)   #Line1
        midPoint(89, 470, 99, 460)  #Line1

        midPoint(180,460,190,470)   #Line2
        midPoint(181,460,191,470)   #Line2

        midPoint(140, 470, 140, 480)  #Line3
        midPoint(142, 470,142,480)   #Line3
        #---------------------------------------------------------------------------------
#------------------------------------------------------------------------

#-----------------------------------HAMMER MAN-----------------------------
def man():
    glPointSize(2)
    glBegin(GL_POINTS)

    #FACE
    glColor3f(0.9098,0.745,0.675)
    drawCircle2(30,300,300)
    radius = 29
    while radius != 0:
        drawCircle2(radius, 300, 300)
        radius -= 1
    glColor3f(0,0,0)
    drawCircle(6,280,305)
    glVertex2f(280,303)
    drawCircle3(8,280,290)

    #TORSO
    glColor3f(0.0,0.211,0.367)
    midPoint(260,170,340,170)
    midPoint(260, 170, 260, 270)
    midPoint(260, 270, 340, 270)
    midPoint(340, 170, 340, 270)
    torso_y = 171
    while torso_y < 271:
        midPoint(260,torso_y,340,torso_y)
        torso_y += 1

    #LEGS
    glColor3f(0.27, 0.07, 0.0)
    midPoint(260, 50, 340, 50)
    midPoint(260, 50, 260, 169)
    midPoint(260, 169, 340, 169)
    midPoint(340, 50, 340, 169)
    pant_y = 51
    while pant_y < 170:
        midPoint(260, pant_y, 340, pant_y)
        pant_y += 1
    glColor3f(0.0,0.0,0.0)

    midPoint(280,50,280,150) #Leg Gap


    glEnd()
#----------------------------------------------------------------
def clouds(scale_factor):
    glPointSize(2)
    glBegin(GL_POINTS)
    cloud_radius = 20 * scale_factor

    # ---------1---------
    temp_radius = cloud_radius
    cloud_x = 350
    cloud_y = 450
    glColor3f(1.0, 1.0, 1.0)
    drawCircle2(temp_radius, cloud_x, cloud_y)
    temp_radius -= 1

    while temp_radius != 0:
        drawCircle2(temp_radius, cloud_x, cloud_y)
        temp_radius -= 1

    # ---------------2--------
    temp_radius = cloud_radius
    cloud_x = 373
    cloud_y = 433
    drawCircle2(temp_radius, cloud_x, cloud_y)
    temp_radius -= 1

    while temp_radius != 0:
        drawCircle2(temp_radius, cloud_x, cloud_y)
        temp_radius -= 1

    # -----------3----------
    temp_radius = cloud_radius
    cloud_x = 370
    cloud_y = 460
    drawCircle2(temp_radius, cloud_x, cloud_y)
    temp_radius -= 1

    while temp_radius != 0:
        drawCircle2(temp_radius, cloud_x, cloud_y)
        temp_radius -= 1

    # -------------4------------
    temp_radius = cloud_radius
    cloud_x = 405
    cloud_y = 450
    drawCircle2(temp_radius, cloud_x, cloud_y)
    temp_radius -= 1

    while temp_radius != 0:
        drawCircle2(temp_radius, cloud_x, cloud_y)
        temp_radius -= 1

    # ---------1.2---------
    temp_radius = cloud_radius
    cloud_x = 250
    cloud_y = 420
    glColor3f(1.0, 1.0, 1.0)
    drawCircle2(temp_radius, cloud_x, cloud_y)
    temp_radius -= 1

    while temp_radius != 0:
        drawCircle2(temp_radius, cloud_x, cloud_y)
        temp_radius -= 1

    # ---------------2.2--------
    temp_radius = cloud_radius
    cloud_x = 273
    cloud_y = 403
    drawCircle2(temp_radius, cloud_x, cloud_y)
    temp_radius -= 1

    while temp_radius != 0:
        drawCircle2(temp_radius, cloud_x, cloud_y)
        temp_radius -= 1

    # -----------3.2----------
    temp_radius = cloud_radius
    cloud_x = 270
    cloud_y = 430
    drawCircle2(temp_radius, cloud_x, cloud_y)
    temp_radius -= 1

    while temp_radius != 0:
        drawCircle2(temp_radius, cloud_x, cloud_y)
        temp_radius -= 1

    # -------------4.2------------
    temp_radius = cloud_radius
    cloud_x = 305
    cloud_y = 420
    drawCircle2(temp_radius, cloud_x, cloud_y)
    temp_radius -= 1

    while temp_radius != 0:
        drawCircle2(temp_radius, cloud_x, cloud_y)
        temp_radius -= 1
    glEnd()

#-------------------------ROTATING HAND HAMMER--------------------------------
def hammer(edge_list,rod_list,hand_list,wrist):
    glPointSize(2)
    glBegin(GL_POINTS)



    glColor3f(0.0, 0.0, 0.0)

    #HAMMER ROD
    rod_y = 222
    count = 8
    while count != 0:
        midPoint(106, rod_y, 223, rod_y)
        rod_list.append(106)
        rod_list.append(rod_y)
        rod_list.append(223)
        rod_list.append(rod_y)
        count -= 1
        rod_y += 1

    #HAMMER EDGE
    glColor3f(0.5, 0.5, 0.5)
    edge_y = 185
    count = 60
    while count != 0:
        midPoint(113, edge_y, 153, edge_y)
        edge_list.append(113)
        edge_list.append(edge_y)
        edge_list.append(153)
        edge_list.append(edge_y)
        count -= 1
        edge_y += 1

    # WRIST
    glColor3f(0.9098, 0.745, 0.675)
    wrist_x = 210
    wrist_y = 225
    wrist.append(210)
    wrist.append(225)
    wrist_radius = 10
    drawCircle2(wrist_radius, wrist_x, wrist_y)
    step = 9
    while step != 0:
        drawCircle2(step, wrist_x, wrist_y)
        step -= 1



    glColor3f(0.0, 0.211, 0.367)
    # HAND
    hand_y = 215
    count = 20
    while count != 0:
        midPoint(220, hand_y, 305, hand_y)
        hand_list.append(220)
        hand_list.append(hand_y)
        hand_list.append(305)
        hand_list.append(hand_y)
        count -= 1
        hand_y += 1

    glEnd()







def iterate():
   glViewport(0, 0, 500, 500)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
   glMatrixMode (GL_MODELVIEW)
   glLoadIdentity()

def showScreen():
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   glLoadIdentity()
   iterate()

   global bar_y1,checker,count,force,takeInputForce,degree,scale_factor,direction,r,edge_list,rod_list,hand_list,wrist,arrow,factor,points


   if takeInputForce == 'Yes':
       print(f'Total Points -----> {points}pts')
       force = int(input("Provide force (N) --->"))

       takeInputForce = 'No'

   scenery()

   #----------------------------------------------------SCALING---------------------------------------
   clouds(scale_factor)
   if (scale_factor == 1) and (direction == 'top'):
       scale_factor = 0.9
       direction = 'mid'
   elif (scale_factor == 0.9) and (direction == 'mid'):
       scale_factor = 0.9
       direction = 'bottom'
   elif (scale_factor == 0.9) and (direction == 'bottom'):
       scale_factor = 1.4
       direction = 'mid'
   elif (scale_factor == 1.4) and (direction == 'mid'):
       scale_factor = 1.2
       direction = 'top'
   elif (scale_factor == 1.2) and (direction == 'top'):
       scale_factor = 1

   #----------------------------------------------------------------

   scale(factor)
   if (factor == 1) and (arrow == 'up'):
       factor = 1.04
       arrow = 'down'
   elif (factor == 1.04) and (arrow == 'down'):
       factor = 1
   elif (factor == 1) and (arrow == 'down'):
       factor = 0.96
       arrow = 'up'
   elif (factor == 0.96) and (arrow == 'up'):
       factor = 1

   #--------------------------------------------------------------
   man()

   #--------------------------------------ROTATION----------------------------------
   if (count == 0) or (count > 4):
       hammer(edge_list,rod_list,hand_list,wrist)
   #-------------------------------------------------------------------------------------
   if 1 <= count < 5:
       glPointSize(2)
       glBegin(GL_POINTS)

       # HAMMER ROD----------------------------------------------------------------------
       for i in range(0, len(rod_list), 4):
           v11 = np.array([[rod_list[i] - 0],
                           [rod_list[i + 1] - 20],
                           [1]])
           v13 = np.array([[rod_list[i + 2] - 0],
                           [rod_list[i + 3] - 20],
                           [1]])

           # rotation
           temp1 = np.matmul(r, v11)
           temp3 = np.matmul(r, v13)

           glColor3f(0, 0, 0)
           midPoint(temp1[0][0] + 0, temp1[1][0] + 20, temp3[0][0] + 0, temp3[1][0] + 20)

           rod_list[i] = temp1[0][0]
           rod_list[i + 1] = temp1[1][0]
           rod_list[i + 2] = temp3[0][0]
           rod_list[i + 3] = temp3[1][0]

       #----------------------------------------------------------------------------------------
       #------------------------------WRIST-----------------------------------------------------
       for i in range(0, len(wrist), 2):
           v11 = np.array([[wrist[i] - 0],
                           [wrist[i + 1] - 20],
                           [1]])
           radius = 10

           # rotation
           temp1 = np.matmul(r, v11)

           glColor3f(0.9098, 0.745, 0.675)
           drawCircle2(radius, temp1[0][0] + 0, temp1[1][0] + 20)

           step = 9
           while step != 0:
               drawCircle2(step, temp1[0][0] + 0, temp1[1][0] + 20)
               step -= 1

           wrist[i] = temp1[0][0]
           wrist[i + 1] = temp1[1][0]


       #HAND------------------------------------------------------------------------------------
       for i in range(0, len(hand_list), 4):
           v11 = np.array([[hand_list[i] - 0],
                           [hand_list[i + 1] - 20],
                           [1]])
           v13 = np.array([[hand_list[i + 2] - 0],
                           [hand_list[i + 3] - 20],
                           [1]])

           # rotation
           temp1 = np.matmul(r, v11)
           temp3 = np.matmul(r, v13)

           glColor3f(0.0,0.211,0.367)
           midPoint(temp1[0][0] + 0, temp1[1][0] + 20, temp3[0][0] + 0, temp3[1][0] + 20)

           hand_list[i] = temp1[0][0]
           hand_list[i + 1] = temp1[1][0]
           hand_list[i + 2] = temp3[0][0]
           hand_list[i + 3] = temp3[1][0]

       # HAMMER EDGE----------------------------------------------------------------------------


       for i in range(0, len(edge_list), 4):
           v11 = np.array([[edge_list[i] - 0],
                           [edge_list[i + 1] - 20],
                           [1]])
           v13 = np.array([[edge_list[i + 2] - 0],
                           [edge_list[i + 3] - 20],
                           [1]])

           # rotation
           temp1 = np.matmul(r, v11)
           temp3 = np.matmul(r, v13)

           glColor3f(0.5, 0.5, 0.5)
           midPoint(temp1[0][0] + 0, temp1[1][0] + 20, temp3[0][0] + 0, temp3[1][0] + 20)

           edge_list[i] = temp1[0][0]
           edge_list[i + 1] = temp1[1][0]
           edge_list[i + 2] = temp3[0][0]
           edge_list[i + 3] = temp3[1][0]
       #--------------------------------------------------------------------------------
       glEnd()

















   if count == 4:
       glPointSize(2)
       glBegin(GL_POINTS)
       glColor3f(0.627, 0.322, 0.176)
       midPoint(60,126,90,122)
       midPoint(190,122,220,126)
       midPoint(90,110,50,105)
       midPoint(190,110,230,105)
       glEnd()


   if count > 4:              #--------------------TRANSLATION--------------------------
       if (5 <= force < 300) and (bar_y1 <= 200) and (checker <= 200):
           bar_y1 += 10
           checker += 10
       elif (5 <= force < 300) and (checker > 200):
           if bar_y1 > 71:
            bar_y1 -= 10
            points += 5
       elif (300 <= force < 600) and (bar_y1 <= 300) and (checker <= 300):
           bar_y1 += 10
           checker += 10
       elif (300 <= force < 600) and (checker > 300):
           if bar_y1 > 71:
            bar_y1 -= 10
            points += 5
       elif (600 <= force < 900) and (bar_y1 <= 420) and (checker <= 420):
           bar_y1 += 10
           checker += 10
       elif (600 <= force < 900) and (checker > 420):
           if bar_y1 > 71:
            bar_y1 -= 10
            points += 5
       elif (force >= 900) and (bar_y1 <= 445) and (checker <= 445):
           bar_y1 += 10
           checker += 10
       elif (force >= 900) and (checker > 445):
           if bar_y1 > 71:
            bar_y1 -= 10
            points += 5

   count += 1

   if (bar_y1 == 71) and (checker != 71):     #----------------RESET-------------------
       bar_y1 = 71
       checker = 71
       count = 0
       force = 0
       edge_list = []
       rod_list = []
       hand_list = []
       wrist = []
       takeInputForce = 'Yes'
   glutPostRedisplay()
   glutSwapBuffers()




glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Hammer Smash!") #window name

bar_y1 = 71
checker = 71
count = 0
force = 0
takeInputForce = 'Yes'
degree = 0.1
scale_factor = 1   #cloud
direction = 'top'
factor = 1  #button
arrow = 'up'
points = 0

edge_list = []
rod_list = []
hand_list = []
wrist = []
a = math.cos(math.radians(degree))
b = math.sin(math.radians(degree))

r = np.array([[a, -b, 0],
              [b, a, 0],
              [0, 0, 1]])

glutDisplayFunc(showScreen)




glutMainLoop()



