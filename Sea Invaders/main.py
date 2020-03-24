import sys

import pygame
from pygame.locals import *

from blaster import Blaster
from fish import Fish
from button import Button

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
TRANSPARENT_GREEN = (0,255,0)

button_transparency = 255
innerm_transparency = 255
outerm_transparency = 128

RUNNING = True

menu = "menu"
outfade = False
infade = False

pygame.init()
screen = pygame.display.set_mode(DIMENSIONS)

sea = pygame.image.load("assets/sea.jpg").convert()

objects = []

def play_resume(outfade):
    outfade = True
    return outfade

startbtn = Button((250, 45), (310,60), play_resume)

menu_transparencies = [button_transparency, innerm_transparency, outerm_transparency]

menuobj_alpha = pygame.Surface(MENUDIMENSIONS, flags=SRCALPHA)
menuobj = pygame.Surface(ACTUALMENUDIMENSIONS, flags=SRCALPHA)

while RUNNING:
    #button_transparency = menu_transparencies[0]
    #innerm_transparency = menu_transparencies[1]
    #outerm_transparency = menu_transparencies[2]
    menu_transparencies = [button_transparency, innerm_transparency, outerm_transparency]
    screen.blit(sea, (0,0))
    screen.blit(sea, (435,0))
    menuobj_alpha.fill((0,255,0,outerm_transparency))
    menuobj.fill((0,255,0,innerm_transparency))
    menuobj_alpha.blit(menuobj, (ACTUALMENUCOORDS[0] - MENUCOORDS[0], ACTUALMENUCOORDS[1] - MENUCOORDS[1]))
    screen.blit(menuobj_alpha, MENUCOORDS)
    startbtn.draw_self(screen, (255,0,0,button_transparency))
    outfade = startbtn.process(outfade)

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                infade = True

    if outfade:
        for i in range(len(menu_transparencies)):
            menu_transparencies[i] -= 8
        button_transparency = menu_transparencies[0]
        innerm_transparency = menu_transparencies[1]
        outerm_transparency = menu_transparencies[2]
        if outerm_transparency < 0: 
            outerm_transparency = 0
        if innerm_transparency < 0: 
            innerm_transparency = 0
        if button_transparency < 0: 
            button_transparency = 0
        if button_transparency == 0 and innerm_transparency == 0 and outerm_transparency == 0:
            outfade = False
    if infade:
        for i in range(len(menu_transparencies)):
            menu_transparencies[i] += 8
        button_transparency = menu_transparencies[0]
        innerm_transparency = menu_transparencies[1]
        outerm_transparency = menu_transparencies[2]
        if outerm_transparency > 128: 
            outerm_transparency = 128
        if innerm_transparency > 255: 
            innerm_transparency = 255
        if button_transparency > 255: 
            button_transparency = 255
        if button_transparency == 255 and innerm_transparency == 255 and outerm_transparency == 128:
            infade = False
    pygame.display.update(screen.get_rect())
