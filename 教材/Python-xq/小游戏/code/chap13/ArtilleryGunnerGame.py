# Artillery Gunner Game
# Chapter 12

import sys, time, random, math, pygame
from pygame.locals import *
from MyLibrary import *


class Terrain():
    def __init__(self, min_height, max_height, total_points):
        self.min_height = min_height
        self.max_height = max_height
        self.total_points = total_points+1
        self.grid_size = 800 / total_points
        self.height_map = list()
        self.generate()
        

    def generate(self):
        #clear list
        if len(self.height_map)>0:
            for n in range(self.total_points):
                self.height_map.pop()
        
        #first point
        last_x = 0
        last_height = (self.max_height + self.min_height) / 2
        self.height_map.append( last_height )
        direction = 1
        run_length = 0
        
        #remaining points
        for n in range( 1, self.total_points ):
            rand_dist = random.randint(1, 10) * direction
            height = last_height + rand_dist
            self.height_map.append( int(height) )
            if height < self.min_height: direction = -1
            elif height > self.max_height: direction = 1
            last_height = height
            if run_length <= 0:
                run_length = random.randint(1,3)
                direction = random.randint(1,2)
                if direction == 2: direction = -1
            else:
                run_length -= 1

    def get_height(self,x):
        x_point = int(x / self.grid_size)
        return self.height_map[x_point]

    def draw(self, surface):
        last_x = 0
        for n in range( 1, self.total_points ):
            #draw circle at current point
            height = 600 - self.height_map[n]
            x_pos = int(n * self.grid_size)
            pos = (x_pos, height)
            color = (255,255,255)
            #pygame.draw.circle(surface, color, pos, 4, 1)
            if n == grid_point:
                pygame.draw.circle(surface, (0,255,0), pos, 4, 0)
            #draw line from previous point
            last_height = 600 - self.height_map[n-1]
            last_pos = (last_x, last_height)
            pygame.draw.line(surface, color, last_pos, pos, 2)
            last_x = x_pos
        
    

# this function initializes the game
def game_init():
    global screen, backbuffer, font, timer, crosshair, crosshair_group, terrain

    pygame.init()
    screen = pygame.display.set_mode((800,600))
    backbuffer = pygame.Surface((800,600))
    pygame.display.set_caption("Artillery Gunner Game")
    font = pygame.font.Font(None, 30)
    timer = pygame.time.Clock()

    #create terrain
    terrain = Terrain(50, 400, 100)

   
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


# these functions draw a cannon at the specified position
def draw_player_cannon(surface,position):
    #draw turret
    turret_color = (30,180,30)
    start_x = position.x + 15
    start_y = position.y + 15
    start_pos = (start_x, start_y)
    vel = angular_velocity( wrap_angle(player_cannon_angle-90) )
    end_pos = (start_x + vel.x * 30, start_y + vel.y * 30)
    pygame.draw.line(surface, turret_color, start_pos, end_pos, 6)
    #draw body
    body_color = (30,220,30)
    rect = Rect(position.x, position.y+15, 30, 15)
    pygame.draw.rect(surface, body_color, rect, 0)
    pygame.draw.circle(surface, body_color, (position.x+15,position.y+15), 15, 0)


def draw_computer_cannon(surface,position):
    #draw turret
    turret_color = (180,30,30)
    start_x = position.x + 15
    start_y = position.y + 15
    start_pos = (start_x, start_y)
    vel = angular_velocity( wrap_angle(computer_cannon_angle-90) )
    end_pos = (start_x + vel.x * 30, start_y + vel.y * 30)
    pygame.draw.line(surface, turret_color, start_pos, end_pos, 6)
    #draw body
    body_color = (220,30,30)
    rect = Rect(position.x, position.y+15, 30, 15)
    pygame.draw.rect(surface, body_color, rect, 0)
    pygame.draw.circle(surface, body_color, (position.x+15,position.y+15), 15, 0)
    


#main program begins
game_init()
audio_init()
game_over = False
player_score = 0
enemy_score = 0
last_time = 0
mouse_x = mouse_y = 0
grid_point = 0
player_score = computer_score = 0
player_cannon_position = Point(0,0)
player_cannon_angle = 45
player_cannon_power = 8.0
computer_cannon_position = Point(0,0)
computer_cannon_angle = 315
computer_cannon_power = 8.0
player_firing = False
player_shell_position = Point(0,0)
player_shell_velocity = Point(0,0)
computer_firing = False
computer_shell_position = Point(0,0)
computer_shell_velocity = Point(0,0)

#main loop
while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()

    #event section
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x,mouse_y = event.pos
        elif event.type == MOUSEBUTTONUP:
            terrain.generate()

    #get key states 
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: sys.exit()

    elif keys[K_UP] or keys[K_w]:
        player_cannon_angle = wrap_angle( player_cannon_angle - 1 )
        
    elif keys[K_DOWN] or keys[K_s]:
        player_cannon_angle = wrap_angle( player_cannon_angle + 1 )

    elif keys[K_RIGHT] or keys[K_d]:
        if player_cannon_power <= 10.0:
            player_cannon_power += 0.1
        
    elif keys[K_LEFT] or keys[K_a]:
        if player_cannon_power > 0.0:
            player_cannon_power -= 0.1
    
    if keys[K_SPACE]:
        if not player_firing:
            play_sound(shoot_sound)
            player_firing = True
            angle = wrap_angle( player_cannon_angle - 90 )
            player_shell_velocity = angular_velocity( angle )
            player_shell_velocity.x *= player_cannon_power
            player_shell_velocity.y *= player_cannon_power
            player_shell_position = player_cannon_position
            player_shell_position.x += 15
            player_shell_position.y += 15
        

    #update section
    if not game_over:
        #keep turret inside a reasonable range
        if player_cannon_angle > 180:
            if player_cannon_angle < 270: player_cannon_angle = 270
        elif player_cannon_angle <= 180:
            if player_cannon_angle > 90: player_cannon_angle = 90
        

        #calculate mouse position on terrain
        grid_point = int(mouse_x / terrain.grid_size)

        #move player shell
        if player_firing:
            player_shell_position.x += player_shell_velocity.x
            player_shell_position.y += player_shell_velocity.y

            #has shell hit terrain?
            height = 600 - terrain.get_height(player_shell_position.x)
            if player_shell_position.y > height:
                player_firing = False

            if player_shell_velocity.y < 10.0:
                player_shell_velocity.y += 0.1

            #has shell gone off the screen?            
            if player_shell_position.x < 0 or player_shell_position.x > 800:
                player_firing = False
            if player_shell_position.y < 0 or player_shell_position.y > 600:
                player_firing = False


        #move computer shell
        if computer_firing:
            computer_shell_position.x += computer_shell_velocity.x
            computer_shell_position.y += computer_shell_velocity.y

            #has shell hit terrain?
            height = 600 - terrain.get_height(computer_shell_position.x)
            if computer_shell_position.y > height:
                computer_firing = False

            if computer_shell_velocity.y < 10.0:
                computer_shell_velocity.y += 0.1
            
            #has shell gone off the screen?
            if computer_shell_position.x < 0 or computer_shell_position.x > 800:
                computer_firing = False
            if computer_shell_position.y < 0 or computer_shell_position.y > 600:
                computer_firing = False
        else:
            #is the computer ready to fire?
            play_sound(shoot_sound)
            computer_firing = True
            computer_cannon_power = random.randint(1,10)
            angle = wrap_angle( computer_cannon_angle - 90 )
            computer_shell_velocity = angular_velocity( angle )
            computer_shell_velocity.x *= computer_cannon_power
            computer_shell_velocity.y *= computer_cannon_power
            computer_shell_position = computer_cannon_position
            computer_shell_position.x += 15
            computer_shell_position.y += 15

        #look for a hit by player's shell
        if player_firing:
            dist = distance(player_shell_position, computer_cannon_position)
            if dist < 30:
                play_sound(boom_sound)
                player_score += 1
                player_firing = False


        #look for a hit by computer's shell
        if computer_firing:
            dist = distance(computer_shell_position, player_cannon_position)
            if dist < 30:
                play_sound(boom_sound)
                computer_score += 1
                computer_firing = False
            


    #drawing section
    backbuffer.fill((20,20,120))

    #draw the terrain
    terrain.draw(backbuffer)

    #draw player's gun
    y = 600 - terrain.get_height(70+15) - 20
    player_cannon_position = Point(70,y)
    draw_player_cannon(backbuffer, player_cannon_position)

    #draw computer's gun
    y = 600 - terrain.get_height(700+15) - 20
    computer_cannon_position = Point(700,y)
    draw_computer_cannon(backbuffer, computer_cannon_position)

    #draw player's shell
    if player_firing:
        x = int(player_shell_position.x)
        y = int(player_shell_position.y)
        pygame.draw.circle(backbuffer, (20,230,20), (x,y), 4, 0)

    #draw computer's shell
    if computer_firing:
        x = int(computer_shell_position.x)
        y = int(computer_shell_position.y)
        pygame.draw.circle(backbuffer, (230,20,20), (x,y), 4, 0)

        
    #draw the back buffer
    screen.blit(backbuffer, (0,0))

    if not game_over:
        print_text(font, 0, 0, "SCORE " + str(player_score))
        print_text(font, 0, 20, "ANGLE " + "{:.1f}".format(player_cannon_angle))
        print_text(font, 0, 40, "POWER " + "{:.2f}".format(player_cannon_power))
        if player_firing:
            print_text(font, 0, 60, "FIRING")
        print_text(font, 650, 0, "SCORE " + str(computer_score))
        print_text(font, 650, 20, "ANGLE " + "{:.1f}".format(computer_cannon_angle))
        print_text(font, 650, 40, "POWER " + "{:.2f}".format(computer_cannon_power))
        if computer_firing:
            print_text(font, 650, 60, "FIRING")

        print_text(font, 0, 580, "CURSOR " + str(Point(mouse_x,mouse_y)) + \
            ", GRID POINT " + str(grid_point) + ", HEIGHT " + \
            str(terrain.get_height(mouse_x)))
    else:
        print_text(font, 0, 0, "GAME OVER")

    pygame.display.update()

    
