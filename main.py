import pygame as pg
import random as random

# The length X height of the window of program
width , height = 700, 950


# Defining clock
clock = pg.time.Clock()


# Initialization of the Program
pg.init()


# Making the screen/Surface
screen = pg.display.set_mode((width,height))


# Making the actual Bird
class Player:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size

        self.speed = 0

        self.jump_speed = 5
        self.fall_speed = 2
        self.max_speed = 7
        

    def movement(self,dt):
        keys = pg.key.get_pressed()

        if keys[pg.K_SPACE]:
            self.speed -= self.jump_speed * dt
        else:   
            self.speed += self.fall_speed * dt

        self.speed = max(-self.max_speed, min(self.speed, self.max_speed))
    def update(self,dt):

        self.y += self.speed

    def draw_player(self,surface):
        pg.draw.rect(surface, (255,255,255), (self.x,int(self.y),self.size,self.size))


# The "Pipes" / blocks / obstacles
class Pipes:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 5

    def update(self):
        self.x -= self.speed
        if self.x < -self.w:
            self.x = width
            self.y = random.randint(-300,0)
    def draw_pipes(self,surface):
        pg.draw.rect(surface , (0,200,0) , (self.x,self.y,self.w,self.h))
        

pipe1 = Pipes(width,random.randint(-300,-200),30,500)

size = 40
bird = Player(width//2,height//2,size)
#Main Game Loop
running = True
while running:
    dt = clock.tick(60) / 1000

    # Checking for exit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    
    # Filling the screen with the bg color
    screen.fill((0,0,0))

    bird.movement(dt)

    bird.update(dt)

    pipe1.update()

    pipe1.draw_pipes(screen)

    bird.draw_player(screen)


    # Flipping the frame buffer to show next changes
    pg.display.flip()

