
## change these paths accordingly
background_image_fp = 'background.jpg'
sprite_image_fp = 'ornament.png'

import pygame
from pygame.locals import *
from sys import exit
import time

pygame.init()

screen = pygame.display.set_mode((200, 200), HWSURFACE | DOUBLEBUF, 32)
pygame.display.set_caption("Horizontal Spraight Movement")

## convert the image to the display's format
background_img = pygame.image.load(background_image_fp).convert()
sprite_img = pygame.image.load(sprite_image_fp)

sprite_x = 0
x_delta = 10
sleep_time = 0.5
## move sprite_img x_delta every sleep_time seconds
my_event = pygame.event.Event(KEYDOWN, key=K_SPACE, mod=0, unicode=u' ')

while True:
    pygame.event.post(my_event)
    for event in pygame.event.get():
        if event.type == QUIT:
            del background_img
            del sprite_img
            pygame.display.quit()
            exit(0)

        screen.blit(background_img, (0, 0))
        screen.blit(sprite_img, (sprite_x, 80))

        sprite_x += x_delta

        if sprite_x > 200.0: sprite_x -= 210.0

        pygame.display.update()
        time.sleep(sleep_time)
    
