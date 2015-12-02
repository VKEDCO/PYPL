#!/usr/bin/python

__metaclass__ = type

import random
import pygame
from pygame.locals import *
import GameParams

class Health(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = Color('white')
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(550, 450)

    def update(self):
        if GameParams.HEALTH != self.lastscore:
            self.lastscore = GameParams.HEALTH
            msg = "HEALTH: %d" % GameParams.HEALTH
            self.image = self.font.render(msg, 0, self.color)
