# Snake Game
# Chapter 11

import sys, time, random, math, pygame
from pygame.locals import *
from MyLibrary import *


class Food(MySprite):
    def __init__(self):
        MySprite.__init__(self)
        image = pygame.Surface((32,32)).convert_alpha()
        image.fill((255,255,255,0))
        pygame.draw.circle(image, (250,250,50), (16,16), 16, 0)
        self.set_image(image)
        MySprite.update(self, 0, 30) #create frame image
        self.X = random.randint(0,23) * 32
        self.Y = random.randint(0,17) * 32
        
class SnakeSegment(MySprite):
    def __init__(self,color=(20,200,20)):
        MySprite.__init__(self)
        image = pygame.Surface((32,32)).convert_alpha()
        image.fill((255,255,255,0))
        pygame.draw.circle(image, color, (16,16), 16, 0)
        self.set_image(image)
        MySprite.update(self, 0, 30) #create frame image

class Snake():
    def __init__(self):
        self.velocity = Point(-1,0)
        self.old_time = 0
        head = SnakeSegment((50,250,50))
        head.X = 12*32
        head.Y = 9*32
        self.segments = list()
        self.segments.append(head)
        self.add_segment()
        self.add_segment()

    def update(self,ticks):
        global step_time #additional code
        if ticks > self.old_time + step_time: #modified code
            self.old_time = ticks
            #move body segments
            for n in range(len(self.segments)-1, 0, -1):
                self.segments[n].X = self.segments[n-1].X
                self.segments[n].Y = self.segments[n-1].Y
            #move snake head
            self.segments[0].X += self.velocity.x * 32
            self.segments[0].Y += self.velocity.y * 32

    def draw(self,surface):
        for segment in self.segments: 
            surface.blit(segment.image, (segment.X, segment.Y))
    
    def add_segment(self):
        last = len(self.segments)-1
        segment = SnakeSegment()
        start = Point(0,0)
        if self.velocity.x < 0: start.x = 32
        elif self.velocity.x > 0: start.x = -32
        if self.velocity.y < 0: start.y = 32
        elif self.velocity.y > 0: start.y = -32
        segment.X = self.segments[last].X + start.x
        segment.Y = self.segments[last].Y + start.y
        self.segments.append(segment)


#this function gets the snake's current direction
def get_current_direction():
    global head_x,head_y
    first_segment_x = snake.segments[1].X//32
    first_segment_y = snake.segments[1].Y//32
    if head_x-1 == first_segment_x:   return "right"
    elif head_x+1 == first_segment_x: return "left"
    elif head_y-1 == first_segment_y: return "down"
    elif head_y+1 == first_segment_y: return "up"
        

#this function gets the direction to the food
def get_food_direction():
    global head_x,head_y
    food = Point(0,0)
    for obj in food_group:
        food = Point(obj.X//32,obj.Y//32)
    if head_x < food.x:       return "right"
    elif head_x > food.x:     return "left"
    elif head_x == food.x:
        if head_y < food.y:   return "down"
        elif head_y > food.y: return "up"

#this function causes snake to move automatically
def auto_move():
    direction = get_current_direction()
    food_dir = get_food_direction()
    if food_dir == "left":
        if direction != "right":
            direction = "left"
    elif food_dir == "right":
        if direction != "left":
            direction = "right"
    elif food_dir == "up":
        if direction != "down":
            direction = "up"
    elif food_dir == "down":
        if direction != "up":
            direction = "down"

    #set velocity based on direction
    if direction == "up": snake.velocity = Point(0,-1)
    elif direction == "down": snake.velocity = Point(0,1)
    elif direction == "left": snake.velocity = Point(-1,0)
    elif direction == "right": snake.velocity = Point(1,0)

    
#this function initializes the game
def game_init():
    global screen, backbuffer, font, timer, snake, food_group

    pygame.init()
    screen = pygame.display.set_mode((24*32,18*32))
    pygame.display.set_caption("Snake Game")
    font = pygame.font.Font(None, 30)
    timer = pygame.time.Clock()

    #create a drawing surface
    backbuffer = pygame.Surface((screen.get_rect().width,screen.get_rect().height))

    #create snake
    snake = Snake()
    image = pygame.Surface((60,60)).convert_alpha()
    image.fill((255,255,255,0))
    pygame.draw.circle(image, (80,80,220,70), (30,30), 30, 0)
    pygame.draw.circle(image, (80,80,250,255), (30,30), 30, 4)

    #create food
    food_group = pygame.sprite.Group()
    food = Food()
    food_group.add(food)


#main program begins
game_init()
game_over = False
last_time = 0

auto_play = False #additional code added
step_time = 400

#main loop
while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()

    #event section
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: sys.exit()
    elif keys[K_UP] or keys[K_w]:
        snake.velocity = Point(0,-1)
    elif keys[K_DOWN] or keys[K_s]:
        snake.velocity = Point(0,1)
    elif keys[K_LEFT] or keys[K_a]:
        snake.velocity = Point(-1,0)
    elif keys[K_RIGHT] or keys[K_d]:
        snake.velocity = Point(1,0)
    elif keys[K_SPACE]: #additional code added
        if auto_play:
            auto_play = False
            step_time = 400
        else:
            auto_play = True
            step_time = 100

    #update section
    if not game_over:
        snake.update(ticks)
        food_group.update(ticks)
        
        #try to pick up food
        hit_list = pygame.sprite.groupcollide(snake.segments, \
            food_group, False, True)
        if len(hit_list) > 0:
            food_group.add(Food())
            snake.add_segment()

        #see if head collides with body
        for n in range(1, len(snake.segments)):
            if pygame.sprite.collide_rect(snake.segments[0], snake.segments[n]):
                game_over = True

        #check screen boundary
        head_x = snake.segments[0].X//32
        head_y = snake.segments[0].Y//32
        if head_x < 0 or head_x > 24 or head_y < 0 or head_y > 18:
            game_over = True

        #additional code added
        if auto_play: auto_move()
    

    #drawing section
    backbuffer.fill((20,50,20)) 
    snake.draw(backbuffer)
    food_group.draw(backbuffer)
    screen.blit(backbuffer, (0,0))

    if not game_over:
        print_text(font, 0, 0, "Length " + str(len(snake.segments)))
        print_text(font, 0, 20, "Position " + str(snake.segments[0].X//32) + \
                   "," + str(snake.segments[0].Y//32))
    else:
        print_text(font, 0, 0, "GAME OVER")

    #additional code added
    if auto_play: 
        print_text(font, 700, 0, "AUTO")
        
   
    pygame.display.update() 
    


