import pygame, random
from pygame.locals import *

class Button():
    """A simple button class"""
    def __init__(self, dim, coords, onclick):
        self.dimensions = dim
        self.coords = coords
        self.callback = onclick
        self.surface = pygame.Surface(self.dimensions, flags=SRCALPHA)
        self.pressed = False
        self.visible = True
    
    def draw_self(self, inputsurface, colour) -> None:
        """Draw the button onto the screen passed as inputsurface with colour colour"""
        self.surface.fill(colour)
        inputsurface.blit(self.surface, self.coords)

    def process(self, callback_params) -> list:
        """Takes the current menustatus and tests if the button has been clicked (falling edge detection). If it has, runs the callback. Otherwise, return the current menustatus"""
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
                        if self.visible:
                            return self.callback()
        return callback_params