#!/usr/bin/python

__metaclass__ = type

import random
import pygame
from pygame.locals import *
import GameParams

class Flower(pygame.sprite.Sprite):
    SPEED = 5
    
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = img
        self.rect = self.image.get_rect(center=(random.choice([100, 200, 300, 400, 500]),0))
        self.frame = 0
        
    def update(self):
        self.rect.move_ip(0, Flower.SPEED)
        self.frame = self.frame + 1
