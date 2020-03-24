import sys

import pygame
from pygame.locals import *

WIDTH, HEIGHT = 640, 480
FPS = 30
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

RUNNING = True

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

while RUNNING:
    screen.fill(GREEN)
    pygame.display.update(screen.get_rect())

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()