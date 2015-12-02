#!/usr/bin/python

import pygame
from pygame.locals import *

MOTH_ODDS      = 2    # chances a new moth appears
FLOWER_ODDS    = 10   # chances a new flower appears
FRAME_RELOAD   = 30   # frames between new flowers and moths
SCREENRECT     = Rect(0, 0, 640, 480)
SCORE          = 0
HEALTH         = 10
