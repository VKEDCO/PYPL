#!/usr/bin/python

# bugs to vladimir dot kulyukin at gmail dot com
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
screen_fill = (255, 255, 255)
screen.fill(screen_fill)
pygame.display.set_caption('Random Circles')
points = []

def rand_rgb():
    return randint(0, 255), randint(0, 255), randint(0, 255)

def rand_screen_pos(width, height):
    return randint(0, width-1), randint(0, height-1)

def rand_screen_pos_wh(wh):
    return randint(0, wh[0]-1), randint(0, wh[1]-1)

### move the mouse inside of the screen to see more and more
### pixels assume random colors
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            exit(0)

        pygame.draw.circle(screen,
                          rand_rgb(), ## color
                          rand_screen_pos_wh(screen.get_size()), ## position
                          randint(0, 200) ## radius
                          )
                          
            
        pygame.display.update()






