# Drawing Lines
# Python 3.2

import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Lines")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0,0,200))
    
    #draw the line
    color = 255,255,0
    width = 8
    pygame.draw.line(screen, color, (100,100), (500,400), width)
    
    pygame.display.update()

