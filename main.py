import pygame as pg
import random as random

# The length X height of the window of program
width , height = 700, 950


# Initialization of the Program
pg.init()


# Making the screen/Surface
screen = pg.display.set_mode((width,height))


#Main Game Loop
running = True
while running:


    # Checking for exit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    
    # Filling the screen with the bg color
    screen.fill((0,0,0))


    # Flipping the frame buffer to show next changes
    pg.display.flip()

