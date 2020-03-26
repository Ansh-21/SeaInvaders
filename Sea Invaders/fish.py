from collector import ObjectCollector
from debugging import debug

from random import choice, randint

import pygame
from pygame.locals import *

class Fish(ObjectCollector, pygame.sprite.Sprite):
    """A class representing the 'ships' that fly towards the player. As this is underwater, we have fish instead!"""
    def __init__(self, DIMENSIONS, SPEED, STILLFRAMES_MAX):
        self.objtype = "fish"
        ObjectCollector.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.type = choice(["fish1", "fish2"])
        self.fishname = "assets/fish/" + self.type + ".png"
        self.surface = pygame.Surface((109, 71), flags=SRCALPHA)
        self.surface.fill((255,255,255,0))
        self.surface.blit(pygame.image.load(self.fishname), (0,0))
        self.surface = pygame.transform.rotate(self.surface, 90)
        self.x = randint(10, DIMENSIONS[0] - 50)
        self.y = 20
        self.SPEED = SPEED
        self.WINDOWHEIGHT = DIMENSIONS[1]
        self.dead = False
        self.moving = False
        self.stillframes = randint(30, STILLFRAMES_MAX)

    def process(self, game, display, debug=False):
        """Processes fish movement down the screen"""
        if not self.dead:
            if self.moving:
                self.y += self.SPEED
            self.draw_self(display)
            if self.y > self.WINDOWHEIGHT + 100:
                self.dead = True
                if debug:
                    print("fish type: " + self.type + ", x: " + str(self.x) + " deleted")
            else:
                if self.stillframes == 0:
                    self.moving = True
                else:
                    self.stillframes -= 1

    def draw_self(self, display):
        display.blit(self.surface, (self.x, self.y))

    def bullet_process(self, bullet):
        return