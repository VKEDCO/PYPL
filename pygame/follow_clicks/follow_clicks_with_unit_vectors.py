#!/usr/bin/python

## click in the window to get the sprite moving

import pygame
from pygame.locals import *
from sys import exit

from vector2d import *

pygame.init()

background_image_fp = 'background.jpg'
sprite_image_fp = 'ornament.png'

screen = pygame.display.set_mode((225, 225), 0, 32)
pygame.display.set_caption("Follow Mouse Clicks")

## convert the image to the display's format
background_img = pygame.image.load(background_image_fp).convert()
sprite_img = pygame.image.load(sprite_image_fp)

clock = pygame.time.Clock()
screen_w = screen.get_width()
screen_h = screen.get_height()
sprite_half_w = int(sprite_img.get_width()/2.0)
sprite_half_h = int(sprite_img.get_height()/2.0)

position_vec = Vector2D(100, 100)
position_point = position_vec.to_point()
destination_point = None
speed = 100
heading_unit_vec = Vector2D()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            del background_img
            del sprite_img
            pygame.display.quit()
            exit(0)

        if event.type == MOUSEBUTTONDOWN:
            ## compute the destination point x and y from the mouse click
            destination_x = event.pos[0] - sprite_half_w
            destination_y = event.pos[1] - sprite_half_h
            destination_point = destination_x, destination_y
            position_point = position_vec.to_int_point()
            heading_unit_vec = Vector2D.vector_from_points(position_point, destination_point)
            heading_unit_vec.normalize()
            print heading_unit_vec.x, heading_unit_vec.y ## for debugging only

    screen.blit(background_img, (0, 0))
    screen.blit(sprite_img, position_point)

    time_passed    = clock.tick() / 1000.0
    distance_moved = time_passed * speed
    move_vec       = heading_unit_vec * distance_moved
    position_vec  += move_vec
    position_point = position_vec.to_int_point()

    pygame.display.update()
