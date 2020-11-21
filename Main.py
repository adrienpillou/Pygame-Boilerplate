import pygame
import os
import sys
from utils import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Constants
TARGET_FPS = 60
HEIGHT = 600 # Screen width
WIDTH = 800 # Screen height
TITLE = "Game's Title"
GAME_RESOLUTION = (WIDTH, HEIGHT) # Base resolution tuple

# Global Variables 
clock = pygame.time.Clock()
running = True

# Window setup & settings
os.environ['SDL_VIDEO_CENTERED'] = '1'
surface = pygame.display.set_mode(GAME_RESOLUTION)
icon = pygame.image.load(os.path.join('assets', 'icon32.png')) 
pygame.display.set_icon(icon) # Custom window icon
pygame.display.set_caption(TITLE)

def start():
    pass

def update(dt):
    draw()
    pygame.display.update()
    pass

def draw():
    surface.fill((0,0,0))
    pass

def quit():
    running = False
    pygame.display.quit()

if __name__ == "__main__":
    # execute only if run as a script
    start()
    while running:
        dt = clock.tick(TARGET_FPS) / 1000
        update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
