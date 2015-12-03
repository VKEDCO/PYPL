import pygame
from pygame.locals import *
from sys import exit

pygame.init()

SCREEN_SIZE = (800, 600)
FONT = pygame.font.SysFont("arial", 16)
FONT_HEIGHT = FONT.get_linesize()
NUM_EVENTS_TO_DISPLAY = SCREEN_SIZE[1]/FONT_HEIGHT
event_texts = []
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

while True:
    ## 1) get an event
    event = pygame.event.wait()
    ## 2) convert the event into a string and append it
    ##    to event_texts
    event_texts.append(str(event))
    ## 3) truncate event_texts to the last NUM_EVENTS_TO_DISPLAY
    event_texts = event_texts[-NUM_EVENTS_TO_DISPLAY:]
    ## 4) if user clicked on X, quit
    if event.type == QUIT:
        del screen
        pygame.display.quit()
        exit(0)
    ## 5) pait screen with white
    screen.fill((255, 255, 255))
    ## 6) display events 
    y = SCREEN_SIZE[1]-FONT_HEIGHT
    for text in reversed(event_texts):
        screen.blit(FONT.render(text, True, (0, 0, 0)), (0, y))
        y -= FONT_HEIGHT
    ## 7) update the display
    pygame.display.update()
