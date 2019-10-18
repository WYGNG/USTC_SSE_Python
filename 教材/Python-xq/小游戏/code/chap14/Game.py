# Roguelike Dungeon Game
# Chapter 14
# mods: print_text(), new SysFont

import sys, time, random, math, pygame
from pygame.locals import *
from MyLibrary import *
from Dungeon import *
from Player import *

def game_init():
    global screen, backbuffer, font1, font2, timer
    pygame.init()
    screen = pygame.display.set_mode((700,650))
    backbuffer = pygame.Surface((700,650))
    pygame.display.set_caption("Dungeon Game")
    font1 = pygame.font.SysFont("Courier New", size=18, bold=True)
    font2 = pygame.font.SysFont("Courier New", size=14, bold=True)
    timer = pygame.time.Clock()

def Die(faces):
    roll = random.randint(1,faces)
    return roll

def playerCollision(stepx,stepy):
    global TILE_EMPTY,TILE_ROOM,TILE_HALL,dungeon,player,level
    yellow = (220,220,0)
    green = (0,220,0)
    
    #get object at location
    char = dungeon.getCharAt(player.x + stepx, player.y + stepy)

    if char == 29: #portal up
        message("portal up")
        
    elif char == 30: #portal down
        message("portal down")
        
    elif char == TILE_EMPTY: #wall
        message("You ran into the wall--ouch!")
        
    elif char == 70: #gold
        gold = random.randint(1,level)
        player.gold += gold
        dungeon.setCharAt(player.x+stepx, player.y+stepy, TILE_ROOM)
        message("You found " + str(gold) + " gold!", yellow)
        
    elif char == 86: #weapon
        weapon = random.randint(1,level+2)
        if level <= 5: #low levels get crappy stuff
            temp = random.randint(0,2)
        else:
            temp = random.randint(3,6)
        if temp == 0: name = "Dagger"
        elif temp == 1: name = "Short Sword"
        elif temp == 2: name = "Wooden Club"
        elif temp == 3: name = "Long Sword"
        elif temp == 4: name = "War Hammer"
        elif temp == 5: name = "Battle Axe"
        elif temp == 6: name = "Halberd"
        if weapon >= player.weapon:
            player.weapon = weapon
            player.weapon_name = name
            message("You found a " + name + " +" + str(weapon) + "!",yellow)
        else:
            player.gold += 1
            message("You discarded a worthless " + name + ".")
        dungeon.setCharAt(player.x+stepx, player.y+stepy, TILE_ROOM)
        
    elif char == 64: #armor
        armor = random.randint(1,level+2)
        if level <= 5: #low levels get crappy stuff
            temp = random.randint(0,2)
        else:
            temp = random.randint(3,7)
        if temp == 0: name = "Cloth"
        elif temp == 1: name = "Patchwork"
        elif temp == 2: name = "Leather"
        elif temp == 3: name = "Chain"
        elif temp == 4: name = "Scale"
        elif temp == 5: name = "Plate"
        elif temp == 6: name = "Mithril"
        elif temp == 7: name = "Adamantium"
        if armor >= player.armor:
            player.armor = armor
            player.armor_name = name
            message("You found a " + name + " +" + str(armor) + "!",yellow)
        else:
            player.gold += 1
            message("You discarded a worthless " + name + ".")
        dungeon.setCharAt(player.x+stepx, player.y+stepy, TILE_ROOM)
        
    elif char == 71: #health
        heal = 0
        for n in range(0,level):
            heal += Die(6)
        player.addHealth(heal)
        dungeon.setCharAt(player.x+stepx, player.y+stepy, TILE_ROOM)
        message("You drank a healing potion worth " + str(heal) + \
            " points!", green)

    elif char == 20: #monster
        attack_monster(player.x + stepx, player.y + stepy, 20)

def attack_monster(x,y,char):
    global dungeon, TILE_ROOM
    
    monster = Monster(dungeon,level,"Grue")

    #player's attack
    defense = monster.getDefense()
    attack = player.getAttack()
    damage = player.getDamage(defense)
    battle_text = "You hit the " + monster.name + " for "
    if attack == 20 + player.str: #critical hit?
        damage *= 2
        battle_text += str(damage) + " CRIT points!"
        dungeon.setCharAt(x, y, 70) #drop gold
    elif attack > defense: #to-hit?
        if damage > 0:
            battle_text += str(damage) + " points."
            dungeon.setCharAt(x, y, 70) #drop gold
        else:
            battle_text += "no damage!"
            damage = 0
    else:
        battle_text = "You missed the " + monster.name + "!"
        damage = 0

    #monster's attack
    defense = player.getDefense()
    attack = monster.getAttack()
    damage = monster.getDamage(defense)
    if attack > defense: #to-hit?
        if damage > 0:
            #if damage is overwhelming, halve it
            if damage > player.max_health: damage /= 2
            battle_text += " It hit you for " + str(damage) + " points."
            player.addHealth(-damage)
        else:
            battle_text += " It no damage to you."
    else:
        battle_text += " It missed you."

    #display battle results
    message(battle_text)

    #did the player survive?
    if player.health <= 0: player.alive = False
    

def move_monsters():
    #find monsters
    for y in range(0,44):
        for x in range(0,79):
            tile = dungeon.getCharAt(x,y)
            if tile == 20: #monster?
                move_monster(x,y,20)

def move_monster(x,y,char):
    global TILE_ROOM
    movex = 0
    movey = 0
    dir = random.randint(1,4)
    if dir == 1: movey = -1
    elif dir == 2: movey = 1
    elif dir == 3: movex = -1
    elif dir == 4: movex = 1
    c = dungeon.getCharAt(x + movex, y + movey)
    if c == TILE_ROOM:
        dungeon.setCharAt(x, y, TILE_ROOM) #delete old position
        dungeon.setCharAt(x+movex, y+movey, char) #move to new position

    
        
def print_stats():
    print_text(font2, 0, 615, "STR")
    print_text(font2, 40, 615, "DEX")
    print_text(font2, 80, 615, "CON")
    print_text(font2, 120, 615, "INT")
    print_text(font2, 160, 615, "CHA")
    print_text(font2, 200, 615, "DEF")
    print_text(font2, 240, 615, "ATT")
    fmt = "{:3.0f}"
    print_text(font2, 0, 630, fmt.format(player.str))
    print_text(font2, 40, 630, fmt.format(player.dex))
    print_text(font2, 80, 630, fmt.format(player.con))
    print_text(font2, 120, 630, fmt.format(player.int))
    print_text(font2, 160, 630, fmt.format(player.cha))
    print_text(font2, 200, 630, fmt.format(player.getDefense()))

    #get average damage
    global att,attlow,atthigh
    att[0] = att[1]
    att[1] = att[2]
    att[2] = att[3]
    att[3] = att[4]
    att[4] = (player.getAttack() + att[0] + att[1] + att[2] + att[3]) // 5
    if att[4] < attlow: attlow = att[4]
    elif att[4] > atthigh: atthigh = att[4]
    print_text(font2, 240, 630, str(attlow) + "-" + str(atthigh))

    print_text(font2, 300, 615, "LVL")
    print_text(font2, 300, 630, fmt.format(player.level))
    print_text(font2, 360, 615, "EXP")
    print_text(font2, 360, 630, str(player.experience))

    print_text(font2, 440, 615, "WPN")
    print_text(font2, 440, 630, str(player.weapon) + ":" + player.weapon_name)
    print_text(font2, 560, 615, "ARM")
    print_text(font2, 560, 630, str(player.armor) + ":" + player.armor_name)

    print_text(font2, 580, 570, "GOLD " + str(player.gold))
    print_text(font2, 580, 585, "HLTH " + str(player.health) + "/" + \
        str(player.max_health))
   
    
def message(text,color=(255,255,255)):
    global message_text, message_color
    message_text = text
    message_color = color


#define ASCII codes used for dungeon
TILE_EMPTY = 177
TILE_ROOM = 31
TILE_HALL = 31

#main program begins
game_init()
game_over = False
last_time = 0
dungeon = Dungeon(30, 30)
dungeon.generate(TILE_EMPTY,TILE_ROOM,TILE_HALL)
player = Player(dungeon, 1, "Player")
player.x = dungeon.entrance_x+1
player.y = dungeon.entrance_y+1
level = 1
message_text = "Welcome, brave adventurer!"
message_color = 0,200,50
draw_radius = False

#used to estimate attack damage
att = list(0 for n in range(0,5))
attlow=90
atthigh=0

#main loop
while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()

    #event section
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE: sys.exit()

            elif event.key == K_TAB:
                #toggle map mode
                draw_radius = not draw_radius
                
            elif event.key == K_SPACE:
                dungeon.generate(TILE_EMPTY,TILE_ROOM,TILE_HALL)
                player.x = dungeon.entrance_x+1
                player.y = dungeon.entrance_y+1
            
            elif event.key==K_UP or event.key==K_w:
                if player.moveUp() == False:
                    playerCollision(0,-1)
                else:
                    move_monsters()
            
            elif event.key==K_DOWN or event.key==K_s:
                if player.moveDown() == False:
                    playerCollision(0,1)
                else:
                    move_monsters()
            
            elif event.key==K_RIGHT or event.key==K_d:
                if player.moveRight() == False:
                    playerCollision(1,0)
                else:
                    move_monsters()
            
            elif event.key==K_LEFT or event.key==K_a:
                if player.moveLeft() == False:
                    playerCollision(-1,0)
                else:
                    move_monsters()
                
        
    #clear the background
    backbuffer.fill((20,20,20))

    #draw the dungeon
    if draw_radius:
        dungeon.draw_radius(backbuffer, player.x, player.y, 6)
    else:
        dungeon.draw(backbuffer)

    #draw the player's little dude        
    player.draw(backbuffer,0)

    #draw the back buffer
    screen.blit(backbuffer, (0,0))

    print_text(font1, 0, 0, "Dungeon Level " + str(level))

    print_text(font1, 600, 0, player.name)

    #special message text
    print_text(font2, 30, 570, message_text, message_color)

    print_stats()
    pygame.display.update()

    
