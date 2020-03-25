## STANDARD IMPORTS
import sys
import random

## PYGAME IMPORTS
import pygame
from pygame.locals import *

## LOCAL IMPORTS
from blaster import Blaster
from fish import Fish
from button import Button
from collector import ObjectCollector

## GAME SIZE CONSTANTS
DIMENSIONS = (870, 520)
MENUCOORDS = (20, 20)
ACTUALMENUCOORDS = (40, 40)
MENUDIMENSIONS = (830, 480)
ACTUALMENUDIMENSIONS = (790, 440)

## GENERAL CONSTANTS
FPS = 30
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
TRANSPARENT_GREEN = (0,255,0)

## TRANSPARENCIES (ALPHA)
button_transparency = 255
innerm_transparency = 255
outerm_transparency = 128
menu_transparencies = [button_transparency, innerm_transparency, outerm_transparency]

## GAME FLOW
RUNNING = True
RESUME = False

## MENU CONTROL
menu = "menu"
menustatus = True
infade = False
outfade = False

## INITIALISATION
pygame.init()
screen = pygame.display.set_mode(DIMENSIONS)

## BACKGROUND
sea = pygame.image.load("assets/sea.jpg").convert()

## CALLBACKS
def play_resume():
    menustatus = False
    topost = True
    return [menustatus, topost]

## BUTTONS
startbtn = Button((250, 45), (310,60), play_resume)

## MENU
menuobj_alpha = pygame.Surface(MENUDIMENSIONS, flags=SRCALPHA)
menuobj = pygame.Surface(ACTUALMENUDIMENSIONS, flags=SRCALPHA)


## MAINLOOP
while RUNNING:
    ## PER-FRAME LOGIC
    menu_transparencies = [button_transparency, innerm_transparency, outerm_transparency]
    prev_menustatus = menustatus

    ## RENDER BACKGROUND
    screen.blit(sea, (0,0))
    screen.blit(sea, (435,0))

    ## RENDER MENU (INCLUDING TRANSPARENCY)
    menuobj_alpha.fill((0,255,0,outerm_transparency))
    menuobj.fill((0,255,0,innerm_transparency))
    screen.blit(menuobj_alpha, MENUCOORDS)
    menuobj_alpha.blit(menuobj, (ACTUALMENUCOORDS[0] - MENUCOORDS[0], ACTUALMENUCOORDS[1] - MENUCOORDS[1]))
    
    ## RENDER BUTTONS
    startbtn.draw_self(screen, (255,0,0,button_transparency))

    ## PROCESS OBJECTS
    menustatus, RESUME = startbtn.process([menustatus, RESUME])
    if not menustatus:
        ObjectCollector.process_all()

    ## EVENT PROCESSING
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                if menustatus:
                    menustatus = False
                else:
                    menustatus = True

    ## CUSTOM EVENT PROCESSING
    if RESUME:
        print("Resume event processed")
        RESUME = False

    ## MENU LOGIC
    if not menustatus:
        if prev_menustatus:
            outfade = True

    if menustatus:
        if not prev_menustatus:
            infade = True

    ## FADING LOGIC
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
            startbtn.visible = False

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
            startbtn.visible = True


    ## UPDATE DISPLAY
    pygame.display.update(screen.get_rect())
