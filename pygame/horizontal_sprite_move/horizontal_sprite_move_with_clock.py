import pygame
from pygame.locals import *
from sys import exit

pygame.init()

## change these paths to your png images that you
## want to be the background and the sprite.
background_image_fp = 'background.jpg'
sprite_image_fp = 'ornament.png'

screen = pygame.display.set_mode((225, 225), 0, 32)
pygame.display.set_caption('Clocked 2D H-Movement')

## convert the image to the display's format
background_img = pygame.image.load(background_image_fp).convert()
sprite_img = pygame.image.load(sprite_image_fp)

clock = pygame.time.Clock()

sprite_x = 0
sprite_y = 100
speed = 15 ## pix/sec
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
        screen.blit(sprite_img, (int(sprite_x), sprite_y))

        time_passed = clock.tick() / 1000.0
        distance_delta = speed * time_passed
        sprite_x += distance_delta

        if sprite_x > 225.0: sprite_x -= 225.0
        pygame.display.update()
