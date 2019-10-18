# MyLibrary.py

import sys, time, random, math, pygame
from pygame.locals import *


# calculates distance between two points
def distance(point1, point2):
    delta_x = point1.x - point2.x
    delta_y = point1.y - point2.y
    dist = math.sqrt(delta_x*delta_x + delta_y*delta_y)
    return dist


# calculates velocity of an angle
def angular_velocity(angle):
    vel = Point(0,0)
    vel.x = math.cos( math.radians(angle) )
    vel.y = math.sin( math.radians(angle) )
    return vel
    
# calculates angle between two points
def target_angle(x1,y1,x2,y2):
    delta_x = x2 - x1
    delta_y = y2 - y1
    angle_radians = math.atan2(delta_y,delta_x)
    angle_degrees = math.degrees(angle_radians)
    return angle_degrees
    
    
# wraps a degree angle at boundary
def wrap_angle(angle):
    return abs(angle % 360)

# prints text using the supplied font #CHANGE
def print_text(font, x, y, text, color=(255,255,255), target=None): #CHANGE
    imgText = font.render(text, True, color)
    if target == None:
        target = pygame.display.get_surface() 
    target.blit(imgText, (x,y))

# MySprite class extends pygame.sprite.Sprite
class MySprite(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.direction = 0
        self.velocity = Point(0.0,0.0)
        self.rotation = 0.0 
        self.old_rotation = 0.0 

    #X property
    def _getx(self): return self.rect.x
    def _setx(self,value): self.rect.x = value
    X = property(_getx,_setx)

    #Y property
    def _gety(self): return self.rect.y
    def _sety(self,value): self.rect.y = value
    Y = property(_gety,_sety)

    #position property
    def _getpos(self): return self.rect.topleft
    def _setpos(self,pos): self.rect.topleft = pos  
    position = property(_getpos,_setpos)
        

    def load(self, filename, width=0, height=0, columns=1):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.set_image(self.master_image, width, height, columns)

    def set_image(self, image, width=0, height=0, columns=1):
        self.master_image = image
        if width==0 and height==0:
            self.frame_width = image.get_width()
            self.frame_height = image.get_height()
        else:
            self.frame_width = width
            self.frame_height = height
            rect = self.master_image.get_rect()
            self.last_frame = (rect.width//width) * (rect.height//height) - 1
        self.rect = Rect(0,0,self.frame_width,self.frame_height)
        self.columns = columns

    def update(self, current_time, rate=30):
        if self.last_frame > self.first_frame:
            #update animation frame number
            if current_time > self.last_time + rate:
                self.frame += 1
                if self.frame > self.last_frame:
                    self.frame = self.first_frame
                self.last_time = current_time
        else:
            self.frame = self.first_frame

        #build current frame only if it changed
        frame_x = (self.frame % self.columns) * self.frame_width
        frame_y = (self.frame // self.columns) * self.frame_height
        rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
        self.image = self.master_image.subsurface(rect)
        self.old_frame = self.frame


    # this is only used when bypassing Group
    def draw(self, surface):
        surface.blit(self.image, (self.X,self.Y))

    def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + \
               "," + str(self.last_frame) + "," + str(self.frame_width) + \
               "," + str(self.frame_height) + "," + str(self.columns) + \
               "," + str(self.rect)

#Point class
class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    #X property
    def getx(self): return self.__x
    def setx(self, x): self.__x = x
    x = property(getx, setx)

    #Y property
    def gety(self): return self.__y
    def sety(self, y): self.__y = y
    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x,2) + \
            ",Y:" + "{:.0f}".format(self.__y) + "}"
    
