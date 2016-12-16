import pygame, sys,os, math, random, time # importing pygame library along with other stoof
from pygame.locals import * #importing another pygame library
from math import sin, cos, pi, radians

pygame.init() #initializing pygame

window = pygame.display.set_mode((800, 800)) #setting resolution of window
screen = pygame.display.get_surface() #setting surfaces for stuff to be put on
angvel = 0 #Angular velocity
radius = 175
angle = radians(1)

center_of_rotation_x = 0
center_of_rotation_y = 10
x = center_of_rotation_x + radius * cos(angle) #Starting position x
y = center_of_rotation_y - radius * sin(angle) #Starting position y

while 1 :
    keys = pygame.key.get_pressed()
    for event in pygame.event.get(): #loop for every event that occurs
        if event.type == QUIT:
            sys.exit(0) #exit da program

    angle = angle + angvel # New angle, we add angular velocity
    x = round(x + radius * angvel * cos(angle + pi / 2)) # New x
    y = round(y - radius * angvel * sin(angle + pi / 2)) # New y

    if keys[pygame.K_a] :   #Changes
        angvel = -0.1       #
                            #Turn
    if keys[pygame.K_d] :   #
        angvel = 0.1        #Direction

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 800))
    pygame.draw.circle (screen, (0, 255, 0), (0, 0), 175, 3)
    pygame.draw.circle (screen, (255, 0, 0), (0, 0), 150, 3)
    pygame.draw.circle (screen, (100, 100, 100), (int(x), int(y)), 25) #Draw new x,y
    pygame.display.flip() #drawing to screen
    pygame.time.wait(50) #Delays program. Otherwise it runs way too quickl