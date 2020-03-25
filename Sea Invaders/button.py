import pygame
from pygame.locals import *

class Button(object):
    """A simple button class"""
    def __init__(self, dim, coords, onclick):
        self.dimensions = dim
        self.coords = coords
        self.callback = onclick
        self.surface = pygame.Surface(self.dimensions, flags=SRCALPHA)
        self.pressed = False
    
    def draw_self(self, inputsurface, colour):
        self.surface.fill(colour)
        inputsurface.blit(self.surface, self.coords)
        return inputsurface

    def process(self, callback_params):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.pressed_keys = pygame.mouse.get_pressed()
        self.prev_frame_pressed = self.pressed
        if self.pressed_keys[0]:
            self.pressed = True
        else:
            self.pressed = False
        if self.prev_frame_pressed:
            if not self.pressed:
                if self.mouse_x > self.coords[0] and self.mouse_x < (self.coords[0] + self.dimensions[0]):
                    if self.mouse_y > self.coords[1] and self.mouse_y < (self.coords[1] + self.dimensions[1]):
                        return self.callback()
        return callback_params