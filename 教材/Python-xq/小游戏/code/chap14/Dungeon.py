# Roguelike Dungeon Game
# Dungeon class
# Chapter 14

import sys, time, random, math, pygame
from pygame.locals import *
from MyLibrary import *

class Dungeon():
    def __init__(self,offsetx,offsety):
        #create the font sprite
        self.text = MySprite()
        self.text.load("ascii8x12.png", 8, 12, 32)

        #create the level list
        self.tiles = list()
        for n in range(0,80*45):
            self.tiles.append(-1)

        self.offsetx = offsetx
        self.offsety = offsety

        self.generate()

    def generate(self, emptyChar=175, roomChar=218, hallChar=177):
        self.emptyChar = emptyChar
        self.roomChar = roomChar
        self.hallChar = hallChar
        
        #clear existing level
        for index in range(0,80*45):
            self.tiles[index] = emptyChar

        #create random rooms
        PL = 4
        PH = 8
        SL = 5
        SH = 14
        self.rooms = list()
        self.createRoom(0,0,PL,PH,SL,SH)
        self.createRoom(20,0,PL,PH,SL,SH)
        self.createRoom(40,0,PL,PH,SL,SH)
        self.createRoom(60,0,PL,PH,SL,SH)
        self.createRoom(0,22,PL,PH,SL,SH)
        self.createRoom(20,22,PL,PH,SL,SH)
        self.createRoom(40,22,PL,PH,SL,SH)
        self.createRoom(60,22,PL,PH,SL,SH)

        #connect the rooms with halls
        self.createHallRight(self.rooms[0],self.rooms[1],hallChar)
        self.createHallRight(self.rooms[1],self.rooms[2],hallChar)
        self.createHallRight(self.rooms[2],self.rooms[3],hallChar)
        self.createHallRight(self.rooms[4],self.rooms[5],hallChar)
        self.createHallRight(self.rooms[5],self.rooms[6],hallChar)
        self.createHallRight(self.rooms[6],self.rooms[7],hallChar)

        #choose a random northern room to connect with the south
        choice = random.randint(0,3)
        print("choice:" + str(choice) + "," + str(choice+4))
        self.createHallDown(self.rooms[choice],self.rooms[choice+4],hallChar)

        #add rooms to level
        for room in self.rooms:
            for y in range(room.y,room.y+room.height):
                for x in range(room.x,room.x+room.width):
                    self.setCharAt(x, y, roomChar)

        #add entrance portal
        choice = random.randint(0,7)
        self.entrance_x = self.rooms[choice].x + self.rooms[choice].width//2
        self.entrance_y = self.rooms[choice].y + self.rooms[choice].height//2
        self.setCharAt(self.entrance_x,self.entrance_y,29) #entry portal
        print("entrance:",choice,self.entrance_x,self.entrance_y)

        #add entrance and exit portals
        choice2 = random.randint(0,7)
        while choice2 == choice:
            choice2 = random.randint(0,7)
        x = self.rooms[choice2].x + self.rooms[choice2].width//2
        y = self.rooms[choice2].y + self.rooms[choice2].height//2
        self.setCharAt(x,y,30) #exit portal
        print("exit:",choice2,x,y)


        #add random gold
        drops = random.randint(5,20)
        for n in range(1,drops):
            self.putCharInRandomRoom(roomChar,70) #'G'

        #add weapon, armor, and health potiions
        self.putCharInRandomRoom(roomChar,86) #'W'
        self.putCharInRandomRoom(roomChar,64) #'A'
        self.putCharInRandomRoom(roomChar,71) #'H'
        self.putCharInRandomRoom(roomChar,71) #'H'

        #add some monsters
        num = random.randint(5,10)
        for n in range(0,num):
            self.putCharInRandomRoom(roomChar,20)
            

    def putCharInRandomRoom(self,targetChar,itemChar):
        tile = 0
        while tile != targetChar:
            x = random.randint(0,79)
            y = random.randint(0,44)
            tile = self.getCharAt(x,y)
        self.setCharAt(x,y,itemChar) 
        

    def createRoom(self,x,y,rposx,rposy,rsizel,rsizeh):
        room = Rect(x + random.randint(1,rposx),
                    y + random.randint(1,rposy),
                    random.randint(rsizel,rsizeh),
                    random.randint(rsizel,rsizeh))
        self.rooms.append(room)

    def createHallRight(self,src,dst,hallChar):
        pathx = src.x + src.width
        pathy = src.y + random.randint(1,src.height-2)
        self.setCharAt(pathx,pathy,hallChar)
        if pathy > dst.y and pathy < dst.y + dst.height:
            while pathx < dst.x:
                pathx += 1
                self.setCharAt(pathx,pathy,hallChar)
        else:
            while pathx < dst.x+1:
                pathx += 1
                self.setCharAt(pathx,pathy,hallChar)
            if pathy < dst.y+1:
                self.setCharAt(pathx,pathy,hallChar)
                while pathy < dst.y:
                    pathy += 1
                    self.setCharAt(pathx,pathy,hallChar)
            else:
                self.setCharAt(pathx,pathy,hallChar)
                while pathy > dst.y + dst.height:
                    pathy -= 1
                    self.setCharAt(pathx,pathy,hallChar)

    def createHallDown(self,src,dst,hallChar):
        pathx = src.x + random.randint(1,src.width-2)
        pathy = src.y + src.height
        self.setCharAt(pathx,pathy,hallChar)
        if pathx > dst.x and pathx < dst.x + dst.width:
            while pathy < dst.y:
                pathy += 1
                self.setCharAt(pathx,pathy,hallChar)
        else:
            while pathy < dst.y+1:
                pathy += 1
                self.setCharAt(pathx,pathy,hallChar)
            if pathx < dst.x+1:
                self.setCharAt(pathx,pathy,hallChar)
                while pathx < dst.x:
                    pathx += 1
                    self.setCharAt(pathx,pathy,hallChar)
            else:
                self.setCharAt(pathx,pathy,hallChar)
                while pathx > dst.x + dst.width:
                    pathx -= 1
                    self.setCharAt(pathx,pathy,hallChar)
        

    def getCharAt(self, x, y):
        if x < 0 or x > 79 or y < 0 or y > 44:
            print("error: x,y = ", x, y)
            return
        index = y * 80 + x
        if index < 0 or index > 80*45:
            print("error: index = ", index)
            return
        return self.tiles[index]

    def setCharAt(self, x, y, char):
        if x < 0 or x > 79 or y < 0 or y > 44:
            print("error: x,y = ", x, y)
            return
        index = y * 80 + x
        if index < 0 or index > 80*45:
            print("error: index = ", index)
            return
        self.tiles[index] = char

    def draw(self, surface):
        for y in range(0,45):
            for x in range(0,80):
                char = self.getCharAt(x,y)
                if char >= 0 and char <= 255:
                    self.draw_char(surface, x, y, char)
                else:
                    pass #empty tile

    def draw_radius(self, surface, rx, ry, radius):
        left = rx - radius
        if left < 0: left = 0
        top = ry - radius
        if top < 0: top = 0
        right = rx + radius
        if right > 79: right = 79
        bottom = ry + radius
        if bottom > 44: bottom = 44
        
        for y in range(top,bottom):
            for x in range(left,right):
                char = self.getCharAt(x,y)
                if char >= 0 and char <= 255:
                    self.draw_char(surface, x, y, char)


    def draw_char(self, surface, tilex, tiley, char):
        self.text.X = self.offsetx + tilex * 8
        self.text.Y = self.offsety + tiley * 12
        self.text.frame = char
        self.text.last_frame = char
        self.text.update(0)
        self.text.draw(surface)
        
        
        
