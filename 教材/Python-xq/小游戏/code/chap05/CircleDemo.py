# Circle Demo
# Chapter 5

import random, math, pygame
from pygame.locals import *

#main program begins
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Circle Demo")
screen.fill((0,0,100))

pos_x = 300
pos_y = 250
radius = 200
angle = 360

#repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    #increment angle
    angle += 1
    if angle >= 360:
        angle = 0
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color = r,g,b

    #calculate coordinates
    x = math.cos( math.radians(angle) ) * radius
    y = math.sin( math.radians(angle) ) * radius

    #draw one step around the circle
    pos = ( int(pos_x + x), int(pos_y + y) )
    pygame.draw.circle(screen, color, pos, 10, 0)

    
    pygame.display.update()
    

