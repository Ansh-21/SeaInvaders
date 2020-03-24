import sys

import pygame
from pygame.locals import *

from blaster import Blaster
from fish import Fish

DIMENSIONS = (870, 520)
MENUCOORDS = (20, 20)
ACTUALMENUCOORDS = (40, 40)
MENUDIMENSIONS = (830, 480)
ACTUALMENUDIMENSIONS = (790, 440)

FPS = 30
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
TRANSPARENT_GREEN = (0,255,0,128)

RUNNING = True

menu = "start"

pygame.init()
screen = pygame.display.set_mode(DIMENSIONS)

sea = pygame.image.load("assets/sea.jpg").convert()

menuobj_alpha = pygame.Surface(MENUDIMENSIONS, flags=SRCALPHA).convert_alpha()
menuobj = pygame.Surface(ACTUALMENUDIMENSIONS).convert()
menuobj_alpha.fill(TRANSPARENT_GREEN)
menuobj.fill(GREEN)
menuobj_alpha.blit(menuobj, (ACTUALMENUCOORDS[0] - MENUCOORDS[0], ACTUALMENUCOORDS[1] - MENUCOORDS[1]))
fullmenu = menuobj_alpha

while RUNNING:
    screen.blit(sea, (0,0))
    screen.blit(sea, (436,0))

    if menu:
        screen.blit(fullmenu, MENUCOORDS)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

    pygame.display.update(screen.get_rect())
