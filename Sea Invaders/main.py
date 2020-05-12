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
    SPEED = 6 # pixels per frame
    BULLET_COOLDOWN = 30 # frames
    BULLET_SPEED = 4
    MAX_STILLFRAMES = 180

    ## TRANSPARENCIES (ALPHA)
    text_transparency = 255
    button_transparency = 255
    innerm_transparency = 255
    outerm_transparency = 128
    menu_transparencies = [text_transparency, button_transparency, innerm_transparency, outerm_transparency]

    ## GAME FLOW
    running = True
    game = Game(DIMENSIONS, FPS)
    clock = pygame.time.Clock()

    ## MENU CONTROL
    menu = "menu"
    menustatus = False
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
    startbtn = Button((300, 48), (285,240), play_resume)

    ## MENU
    menufont = pygame.font.Font("assets/fonts/PressStart2P.ttf", 40)
    menutext = "Sea Invaders!"
    btnfont = pygame.font.Font("assets/fonts/PressStart2P.ttf", 35)
    btntext = "Start!"
    menuobj_alpha = pygame.Surface(MENUDIMENSIONS, flags=SRCALPHA)
    menuobj = pygame.Surface(ACTUALMENUDIMENSIONS, flags=SRCALPHA)
    score = pygame.font.Font("assets/fonts/PressStart2P.ttf", 25)

    ## FISH SPAWNER INITIALISATION
    spawner = FishController(SPAWNING_SPEED, SPEED, MAX_STILLFRAMES)
    blaster = Blaster(BULLET_COOLDOWN, BULLET_SPEED)


    ## MAINLOOP
    while running:
        ## PER-FRAME LOGIC
        menu_transparencies = [text_transparency, button_transparency, innerm_transparency, outerm_transparency]
        prev_menustatus = menustatus

        ## RENDER BACKGROUND
        screen.blit(sea, (0,0))
        screen.blit(sea, (435,0))

        ## RENDER MENU (INCLUDING TRANSPARENCY)
        menuobj_alpha.fill((0,255,0,outerm_transparency))
        menuobj.fill((0,255,0,innerm_transparency))
        menuobj_alpha.blit(menuobj, (ACTUALMENUCOORDS[0] - MENUCOORDS[0], ACTUALMENUCOORDS[1] - MENUCOORDS[1]))
        menutextsurface = menufont.render(menutext, True, RED)
        menutext_surf = pygame.Surface((menutextsurface.get_rect().width, menutextsurface.get_rect().height))
        menutext_surf.blit(menutextsurface, pygame.Rect(0, 0, 10, 10), special_flags=pygame.BLEND_RGBA_MULT)
        menutext_surf.set_alpha(text_transparency)
        menuobj_alpha.blit(menutext_surf, ((MENUDIMENSIONS[0]/2)-(menutext_surf.get_rect().width/2), 60))
        if menustatus:
            screen.blit(menuobj_alpha, MENUCOORDS)
    
        ## RENDER BUTTONS
        #btntextsurface = menufont.render(menutext, True, GREEN)
        #btntext_surf = pygame.Surface((btntextsurface.get_rect().width, btntextsurface.get_rect().height))
        #btntext_surf.blit(btntextsurface, pygame.Rect(0, 0, 10, 10), special_flags=pygame.BLEND_RGBA_MULT)
        if menustatus:
            startbtn.draw_self(screen, (255,0,0,button_transparency))#, btntext_surf)

        ## PROCESS MENU
        menustatus = startbtn.process(menustatus)

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
        if game.score < 0:
            menustatus = True
            game.score = 0
            ObjectCollector.clear_all()


        if menustatus:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)

        if not menustatus:
            if prev_menustatus:
                outfade = True

        if menustatus:
            if not prev_menustatus:
                infade = True

        ## PROCESS OBJECTS
        if not prev_menustatus:
            if outfade == False:
                game, screen = ObjectCollector.process_all(game, screen)

        ## FADING LOGIC
        if outfade:
            for i in range(len(menu_transparencies)):
                menu_transparencies[i] -= 8
            text_transparency = menu_transparencies[0]
            button_transparency = menu_transparencies[1]
            innerm_transparency = menu_transparencies[2]
            outerm_transparency = menu_transparencies[3]
            if text_transparency < 0: 
                text_transparency = 0
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
            text_transparency = menu_transparencies[0]
            button_transparency = menu_transparencies[1]
            innerm_transparency = menu_transparencies[2]
            outerm_transparency = menu_transparencies[3]
            if outerm_transparency > 128: 
                outerm_transparency = 128
            if innerm_transparency > 255: 
                innerm_transparency = 255
            if button_transparency > 255: 
                button_transparency = 255
            if button_transparency == 255 and innerm_transparency == 255 and outerm_transparency == 128:
                infade = False
                startbtn.visible = True

        ## RENDER SCORE
        score_surf = score.render(str(game.score), True, WHITE)
        screen.blit(score_surf, (70, 70))

        ## UPDATE DISPLAY
        pygame.display.update(screen.get_rect())

        ## FPS TRACKING
        clock.tick(FPS)
        game.increment_frames()

if __name__  == "__main__":
    run()