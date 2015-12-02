#!/usr/bin/env python
__metaclass__ = type

import random
import pygame
from pygame.locals import *
import GameParams

class Bee(pygame.sprite.Sprite):
    SPEED = 10
    
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image    = img
        self.rect     = self.image.get_rect(midbottom=GameParams.SCREENRECT.midbottom)
        self.origtop  = self.rect.top
        
    ## direction comes at object create time. direction is inside
    ## the game loop.
    def move(self, direction):
        self.rect.move_ip(direction * Bee.SPEED, 0)
        self.rect = self.rect.clamp(GameParams.SCREENRECT)
