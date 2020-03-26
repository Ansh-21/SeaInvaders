from collector import ObjectCollector
from random import choice, randint

import pygame
from pygame.locals import *

class Fish(ObjectCollector):
    """A class representing the 'ships' that fly towards the player. As this is underwater, we have fish instead!"""
    def __init__(self, DIMENSIONS, SPEED):
        self.type = "fish"
        ObjectCollector.__init__(self)
        self.fishtype = choice(["fish1", "fish2"])
        self.fishname = "assets/fish/" + self.fishtype + ".png"
        self.surface = pygame.Surface((136, 89), flags=SRCALPHA)
        self.surface.fill((255,255,255,0))
        self.surface.blit(pygame.image.load(self.fishname), (0,0))
        self.surface = pygame.transform.rotate(self.surface, 90)
        self.x = randint(10, DIMENSIONS[0] - 50)
        self.y = 20
        self.speed = SPEED

    def process(self, game):
        """Processes fish movement down the screen"""
        self.y += self.speed

    def draw_self(self, display):
        display.blit(self.surface, (self.x, self.y))