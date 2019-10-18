# Tank Battle Game
# Chapter 12

import sys, time, random, math, pygame
from pygame.locals import *
from MyLibrary import *


class Bullet():
    def __init__(self,position):
        self.alive = True
        self.color = (250,20,20)
        self.position = Point(position.x,position.y)
        self.velocity = Point(0,0)
        self.rect = Rect(0,0,4,4)
        self.owner = ""

    def update(self,ticks):
        self.position.x += self.velocity.x * 10.0
        self.position.y += self.velocity.y * 10.0
        if self.position.x < 0 or self.position.x > 800 \
            or self.position.y < 0 or self.position.y > 600:
                self.alive = False
        self.rect = Rect(self.position.x, self.position.y, 4, 4)

    def draw(self,surface):
        pos = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(surface, self.color, pos, 4, 0)
        
def fire_cannon(tank):
    position = Point(tank.turret.X, tank.turret.Y)
    bullet = Bullet(position)
    angle = tank.turret.rotation
    bullet.velocity = angular_velocity(angle)
    bullets.append(bullet)
    play_sound(shoot_sound)
    return bullet

def player_fire_cannon():
    bullet = fire_cannon(player)
    bullet.owner = "player"
    bullet.color = (30,250,30)

def enemy_fire_cannon():
    bullet = fire_cannon(enemy_tank)
    bullet.owner = "enemy"
    bullet.color = (250,30,30)

    
class Tank(MySprite):
    def __init__(self,tank_file="tank.png",turret_file="turret.png"):
        MySprite.__init__(self)
        self.load(tank_file, 50, 60, 4)
        self.speed = 0.0
        self.scratch = None
        self.float_pos = Point(0,0)
        self.velocity = Point(0,0)
        self.turret = MySprite()
        self.turret.load(turret_file, 32, 64, 4)
        self.fire_timer = 0

    def update(self,ticks):
        #update chassis
        MySprite.update(self,ticks,100)
        self.rotation = wrap_angle(self.rotation)
        self.scratch = pygame.transform.rotate(self.image, -self.rotation)
        angle = wrap_angle(self.rotation-90)
        self.velocity = angular_velocity(angle)
        self.float_pos.x += self.velocity.x 
        self.float_pos.y += self.velocity.y

        #warp tank around screen edges (keep it simple)
        if self.float_pos.x < -50: self.float_pos.x = 800
        elif self.float_pos.x > 800: self.float_pos.x = -50
        if self.float_pos.y < -60: self.float_pos.y = 600
        elif self.float_pos.y > 600: self.float_pos.y = -60

        #transfer float position to integer position for drawing
        self.X = int(self.float_pos.x)
        self.Y = int(self.float_pos.y)
        
        #update turret
        self.turret.position = (self.X,self.Y)
        self.turret.last_frame = 0
        self.turret.update(ticks,100)
        self.turret.rotation = wrap_angle(self.turret.rotation)
        angle = self.turret.rotation+90
        self.turret.scratch = pygame.transform.rotate(self.turret.image, -angle)

    def draw(self,surface):
        #draw the chassis
        width,height = self.scratch.get_size()
        center = Point(width/2,height/2)
        surface.blit(self.scratch, (self.X-center.x, self.Y-center.y))
        #draw the turret        
        width,height = self.turret.scratch.get_size()
        center = Point(width/2,height/2)
        surface.blit(self.turret.scratch, (self.turret.X-center.x,
            tself.turret.Y-center.y))

    def __str__(self):
        return MySprite.__str__(self) + "," + str(self.velocity)

class EnemyTank(Tank):
    def __init__(self,tank_file="enemy_tank.png",turret_file="enemy_turret.png"):
        Tank.__init__(self,tank_file,turret_file)

    def update(self,ticks):
        self.turret.rotation = wrap_angle(self.rotation-90)
        Tank.update(self,ticks)

    def draw(self,surface):
        Tank.draw(self,surface)


#this function initializes the game
def game_init():
    global screen, backbuffer, font, timer, player_group, player, \
           enemy_tank, bullets, crosshair, crosshair_group

    pygame.init()
    screen = pygame.display.set_mode((800,600))
    backbuffer = pygame.Surface((800,600))
    pygame.display.set_caption("Tank Battle Game")
    font = pygame.font.Font(None, 30)
    timer = pygame.time.Clock()
    pygame.mouse.set_visible(False)

    #load mouse cursor
    crosshair = MySprite()
    crosshair.load("crosshair.png")
    crosshair_group = pygame.sprite.GroupSingle()
    crosshair_group.add(crosshair)

    #create player tank
    player = Tank()
    player.float_pos = Point(400,300)

    #create enemy tanks
    enemy_tank = EnemyTank()
    enemy_tank.float_pos = Point(random.randint(50,760), 50)
    enemy_tank.rotation = 135

    #create bullets
    bullets = list()
   
# this function initializes the audio system
def audio_init():
    global shoot_sound, boom_sound

    #initialize the audio mixer
    pygame.mixer.init() 

    #load sound files
    shoot_sound = pygame.mixer.Sound("shoot.wav")
    boom_sound = pygame.mixer.Sound("boom.wav")


# this function uses any available channel to play a sound clip
def play_sound(sound):
    channel = pygame.mixer.find_channel(True)
    channel.set_volume(0.5)
    channel.play(sound)


#main program begins
game_init()
audio_init()
game_over = False
player_score = 0
enemy_score = 0
last_time = 0
mouse_x = mouse_y = 0


#main loop
while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()

    #reset mouse state variables
    mouse_up = mouse_down = 0
    mouse_up_x = mouse_up_y = 0
    mouse_down_x = mouse_down_y = 0
    
    #event section
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x,mouse_y = event.pos
            move_x,move_y = event.rel
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = event.button
            mouse_down_x,mouse_down_y = event.pos
        elif event.type == MOUSEBUTTONUP:
            mouse_up = event.button
            mouse_up_x,mouse_up_y = event.pos

    #get key states            
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: sys.exit()

    elif keys[K_LEFT] or keys[K_a]:
        #calculate new direction velocity
        player.rotation -= 2.0
        
    elif keys[K_RIGHT] or keys[K_d]:
        #calculate new direction velocity
        player.rotation += 2.0

    #fire cannon!
    if keys[K_SPACE] or mouse_up > 0:
        if ticks > player.fire_timer + 1000:
            player.fire_timer = ticks
            player_fire_cannon()

    #update section
    if not game_over:
        crosshair.position = (mouse_x,mouse_y)
        crosshair_group.update(ticks)

        #point tank turret toward crosshair
        angle = target_angle(player.turret.X,player.turret.Y,
            crosshair.X + crosshair.frame_width/2,
            crosshair.Y + crosshair.frame_height/2)
        player.turret.rotation = angle

        #move tank
        player.update(ticks)

        #update enemies
        enemy_tank.update(ticks)
        if ticks > enemy_tank.fire_timer + 1000:
            enemy_tank.fire_timer = ticks
            enemy_fire_cannon() 

        #update bullets
        for bullet in bullets:
            bullet.update(ticks)
            if bullet.owner == "player":
                if pygame.sprite.collide_rect(bullet, enemy_tank):
                    player_score += 1
                    bullet.alive = False
                    play_sound(boom_sound)
            elif bullet.owner == "enemy":
                if pygame.sprite.collide_rect(bullet, player):
                    enemy_score += 1
                    bullet.alive = False
                    play_sound(boom_sound)


    #drawing section
    backbuffer.fill((100,100,20)) 

    for bullet in bullets:
        bullet.draw(backbuffer)

    enemy_tank.draw(backbuffer)

    player.draw(backbuffer)

    crosshair_group.draw(backbuffer)

    screen.blit(backbuffer, (0,0))

    if not game_over:
        print_text(font, 0, 0, "PLAYER " + str(player_score))
        print_text(font, 700, 0, "ENEMY " + str(enemy_score))
    else:
        print_text(font, 0, 0, "GAME OVER")

    pygame.display.update()

    #remove expired bullets
    for bullet in bullets:
        if bullet.alive == False:
            bullets.remove(bullet)

    
