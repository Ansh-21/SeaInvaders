from collector import ObjectCollector

import pygame
from pygame.locals import *

class Bullet(ObjectCollector, pygame.sprite.Sprite):
    """A class representing the bullets shot by the blaster"""
    def __init__(self, x, y, BULLET_SPEED):
        self.objtype = "bullet"
        ObjectCollector.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.surface = pygame.image.load("assets/fish/fish2.png")
        self.surface = pygame.transform.scale(self.surface, (66, 84))
        self.surface = pygame.transform.rotate(self.surface, -90)
        self.SPEED = BULLET_SPEED
        self.dead = False

    def process(self, display):
        if not self.dead:
            self.draw_self(display)
            self.y -= self.SPEED
            if self.y < -100:
                self.dead = True
                ObjectCollector.remove_this("bullets", self)

    def draw_self(self, display):
        display.blit(self.surface, (self.x, self.y))