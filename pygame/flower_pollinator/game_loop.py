#!/usr/bin/env python

import random, os.path

#import basic pygame modules
import pygame
from pygame.locals import *
import GameParams
from Bee import *
from Moth import *
from Flower import *
from Score import *
from Health import *

## if you double click, __file__ is the absolute path to your game
GAME_DIR = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(GAME_DIR, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert_alpha() #To blend in the border pixels

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

def load_sound(file):
    if not pygame.mixer: return dummysound()
    file = os.path.join(GAME_DIR, 'data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print ('Warning, unable to load, %s' % file)

# Initialize pygame
pygame.init()
## pygame.mixer is used for sound files.
if pygame.mixer and not pygame.mixer.get_init():
    print ('Warning, no sound')
    pygame.mixer = None

## Set the display mode
WINSTYLE = 0 # |FULLSCREEN
DEPTH    = pygame.display.mode_ok(GameParams.SCREENRECT.size, WINSTYLE, 32)
SCREEN   = pygame.display.set_mode(GameParams.SCREENRECT.size, WINSTYLE, DEPTH)

## Load images for Bees, Moths, and Flowers
BEE_IMAGE    = load_image('bee.png');
MOTH_IMAGE   = load_image('moth.png')
FLOWER_IMAGE = load_image('flower.png')

## Set the icon and caption
GAME_ICON = pygame.transform.scale(FLOWER_IMAGE, (32, 32))
pygame.display.set_icon(GAME_ICON)
pygame.display.set_caption('Flower Pollinator 1.0')
pygame.mouse.set_visible(0)

## Create a background screen and tile it
BACKGROUND_TILE = load_image('background.gif')
BACKGROUND = pygame.Surface(GameParams.SCREENRECT.size)
for x in range(0, GameParams.SCREENRECT.width, BACKGROUND_TILE.get_width()):
    BACKGROUND.blit(BACKGROUND_TILE, (x, 0))
SCREEN.blit(BACKGROUND, (0,0))
pygame.display.flip()

## Load the sound effects
splash_sound = load_sound('splash.wav')
ding_sound = load_sound('whiff.wav')
if pygame.mixer:
    music = os.path.join(GAME_DIR, 'data', 'BeeSym.wav')
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1) ## play continuously as long as the game is on

def game_loop():
    global BACKGROUND
    global SCREEN
    ## Initialize sprite groups
    MOTHS   = pygame.sprite.Group()
    ALL     = pygame.sprite.RenderUpdates()
    FLOWERS = pygame.sprite.Group()
    if pygame.font:
        ALL.add(Score())
        ALL.add(Health())

    ## Assign default groups to each sprite class
    Bee.containers    = ALL
    Moth.containers   = MOTHS, ALL
    Flower.containers = FLOWERS, ALL
    Score.containers  = ALL
    Health.containers = ALL

    # Create starting values
    FRAME_RELOAD = GameParams.FRAME_RELOAD
    clock = pygame.time.Clock()
    bee = Bee(BEE_IMAGE)
    
    while bee.alive():
        if GameParams.HEALTH == 0: bee.kill()
                
        ## get keyboard intput
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return
        keystate = pygame.key.get_pressed()

        # clear/erase the last drawn sprites
        ALL.clear(SCREEN, BACKGROUND)
        # update all the sprites
        ALL.update()
        # handle user player input and move the bee sprite left/right
        direction = keystate[K_RIGHT] - keystate[K_LEFT]
        bee.move(direction)
       
        # Create new moth
        if FRAME_RELOAD > 0:
            FRAME_RELOAD = FRAME_RELOAD - 1
        elif not int(random.random() * GameParams.MOTH_ODDS) != 0:
            Moth(MOTH_IMAGE)
            FRAME_RELOAD = GameParams.FRAME_RELOAD

        # Create new flower
        if FRAME_RELOAD > 0:
            FRAME_RELOAD = FRAME_RELOAD - 1
        elif not int(random.random() * GameParams.FLOWER_ODDS) != 0:
            Flower(FLOWER_IMAGE)
            FRAME_RELOAD = GameParams.FRAME_RELOAD
      
        ## has the bee collided with the moth?
        for moth in pygame.sprite.spritecollide(bee, MOTHS, 1):
            splash_sound.play()
            GameParams.HEALTH = GameParams.HEALTH - 1

        ## has the bee collieded with a flower?
        for flower in pygame.sprite.spritecollide(bee, FLOWERS, 1):
            ding_sound.play()
            GameParams.SCORE = GameParams.SCORE + 1
        
        ## draw the scene
        drawn_screen = ALL.draw(SCREEN)
        pygame.display.update(drawn_screen)

        ## advance the clock
        clock.tick(40)

    if pygame.mixer: pygame.mixer.music.fadeout(1000)
    pygame.time.wait(1000)
    pygame.quit()

#call the "main" function if running this script
if __name__ == '__main__': game_loop()
