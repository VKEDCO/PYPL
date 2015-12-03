#!/usr/bin/python

## -> moves sprite left
## <- moves sprite right
## up arrow moves sprite up

background_image_fp = 'background.jpg'
sprite_image_fp     = 'ornament.png'

import pygame
from pygame.locals import *
from sys import exit

from vector2d import *

pygame.init()

## screen is a Surface object
## the second parameter is flags (0 means None, in tihs case)
## 32 is depth - number of bits used to store colors
screen = pygame.display.set_mode((225, 225), 0, 32)
pygame.display.set_caption('Arrow Key Movement Control')

## convert the image to the display's format
background_img = pygame.image.load(background_image_fp).convert()
sprite_img = pygame.image.load(sprite_image_fp)

clock = pygame.time.Clock()

screen_w = screen.get_width()
screen_h = screen.get_height()
sprite_half_w = int(sprite_img.get_width()/2.0)
sprite_half_h = int(sprite_img.get_height()/2.0)

position_vec   = Vector2D(100, 0)
position_point = position_vec.to_point()
destination_point = None
speed = 30

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            del background_img
            del sprite_img
            pygame.display.quit()
            exit(0)

    pressed_keys = pygame.key.get_pressed()
    direction_vec = Vector2D(0, 1)
    if pressed_keys[K_LEFT]:
        direction_vec.x = -1
    elif pressed_keys[K_RIGHT]:
        direction_vec.x = +1
    if pressed_keys[K_UP]:
        direction_vec.y = -1
    elif pressed_keys[K_DOWN]:
        direction_vec.y = +1

    direction_vec.normalize()
        
    screen.blit(background_img, (0, 0))
    screen.blit(sprite_img, position_point)

    time_passed = clock.tick() / 1000.0

    distance_moved = time_passed * speed
    position_vec += direction_vec * distance_moved
    position_point = position_vec.to_int_point()

    pygame.display.update()

