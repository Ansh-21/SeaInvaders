from bullet import Bullet
from collector import ObjectCollector
from debugging import *

import pygame
from pygame.locals import *

class Blaster(ObjectCollector):
    """A class representing the blaster that the player plays as."""
    def __init__(self, COOLDOWN, BULLET_SPEED):
        self.objtype = "blaster"
        ObjectCollector.__init__(self)
        self.surface = pygame.image.load("assets/fish/fish1.png")
        self.surface = pygame.transform.rotate(self.surface, -90)
        self.x = 390
        self.y = 422
        self.cooldown = COOLDOWN
        self.active_cooldown = 0
        self.BULLET_SPEED = BULLET_SPEED
        self.pressed = False
        self.font = pygame.font.Font("assets/fonts/PressStart2P.ttf", 25)

    def process(self, display, game, debug=False, automatic=False):
        self.x = pygame.mouse.get_pos()[0] - 45
        self.draw_self(display, game)
        self.pressed_keys = pygame.mouse.get_pressed()

        if self.pressed_keys[0]:
            self.pressed = True
        else:
            self.pressed = False

        if not automatic:
            if self.pressed:
                if self.active_cooldown == 0:
                    bullet = Bullet(self.x, self.y, self.BULLET_SPEED)
                    self.active_cooldown = self.cooldown
        else:
            if self.active_cooldown == 0:
                    bullet = Bullet(self.x, self.y, self.BULLET_SPEED)
                    self.active_cooldown = self.cooldown

        if self.active_cooldown > 0:
            self.active_cooldown -= 1
    
        if debug:
            print(self.active_cooldown)

    def draw_self(self, display, game):
        display.blit(self.surface, (self.x, self.y))
        display.blit(self.font.render("Cooldown: " + str(self.active_cooldown/game.FPS)[:3] + "s", True, (255,255,255)), (0, 0))