import pygame as pg
import random as random

# The length X height of the window of program
width , height = 700, 950


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

        self.jump_speed = 50
        self.fall_speed = 30

    def movement(self,dt):
        pass
    

    def draw_player(self):
        pass



#Main Game Loop
running = True
while running:


    # Checking for exit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    
    # Filling the screen with the bg color
    screen.fill((0,0,0))

    # movement

    
    #drawing


    # Flipping the frame buffer to show next changes
    pg.display.flip()

