## STANDARD IMPORTS
import sys
import random

## PYGAME IMPORTS
import pygame
from pygame.locals import *

## LOCAL IMPORTS
from blaster import Blaster
from button import Button
from collector import ObjectCollector
from game import Game
from fishcontroller import FishController

def run():
    ## GAME SIZE CONSTANTS
    DIMENSIONS = (870, 520)
    MENUCOORDS = (20, 20)
    ACTUALMENUCOORDS = (40, 40)
    MENUDIMENSIONS = (830, 480)
    ACTUALMENUDIMENSIONS = (790, 440)

    ## GENERAL CONSTANTS
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    WHITE = (255,255,255)
    TRANSPARENT_GREEN = (0,255,0)

    ## CUSTOMISATION
    FPS = 30
    SPAWNING_SPEED = 0.25 # spawns per second
    SPEED = 4 # pixels per frame

    ## TRANSPARENCIES (ALPHA)
    button_transparency = 255
    innerm_transparency = 255
    outerm_transparency = 128
    menu_transparencies = [button_transparency, innerm_transparency, outerm_transparency]

    ## GAME FLOW
    running = True
    game = Game(DIMENSIONS, FPS)
    clock = pygame.time.Clock()

    ## MENU CONTROL
    menu = "menu"
    menustatus = True
    infade = False
    outfade = False

    ## INITIALISATION
    pygame.init()
    screen = pygame.display.set_mode(DIMENSIONS)
    pygame.display.set_caption("Sea Invaders!")
    icon = pygame.image.load("assets/icon/icon.jpg")
    pygame.display.set_icon(icon)

    ## BACKGROUND
    sea = pygame.image.load("assets/background/sea.jpg").convert()

    ## CALLBACKS
    def play_resume():
        """Updates and returns the new menustatus. Since this callback is only called to resume the game, sets menustatus to false."""
        menustatus = False
        return menustatus

    ## BUTTONS
    startbtn = Button((250, 45), (310,60), play_resume)

    ## MENU
    menuobj_alpha = pygame.Surface(MENUDIMENSIONS, flags=SRCALPHA)
    menuobj = pygame.Surface(ACTUALMENUDIMENSIONS, flags=SRCALPHA)

    ## FISH SPAWNER INITIALISATION
    spawner = FishController(SPAWNING_SPEED, SPEED)


    ## MAINLOOP
    while running:
        ## PER-FRAME LOGIC
        menu_transparencies = [button_transparency, innerm_transparency, outerm_transparency]
        prev_menustatus = menustatus

        ## RENDER BACKGROUND
        screen.blit(sea, (0,0))
        screen.blit(sea, (435,0))

        ## RENDER MENU (INCLUDING TRANSPARENCY)
        menuobj_alpha.fill((0,255,0,outerm_transparency))
        menuobj.fill((0,255,0,innerm_transparency))
        menuobj_alpha.blit(menuobj, (ACTUALMENUCOORDS[0] - MENUCOORDS[0], ACTUALMENUCOORDS[1] - MENUCOORDS[1]))
        screen.blit(menuobj_alpha, MENUCOORDS)
    
        ## RENDER BUTTONS
        startbtn.draw_self(screen, (255,0,0,button_transparency))

        ## PROCESS OBJECTS
        menustatus = startbtn.process(menustatus)
        if not menustatus:
            game, screen = ObjectCollector.process_all(game, screen)

        ## EVENT PROCESSING
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if not infade and not outfade:
                        if menustatus:
                            menustatus = False
                        else:
                            menustatus = True

        ## CUSTOM EVENT PROCESSING

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

        ## FPS TRACKING
        clock.tick(FPS)
        game.increment_frames()

if __name__  == "__main__":
    run()