"""
Game settings
© Andboogl, 2024
"""


import os
import pygame


WINDOW_SIZE = (1200, 800)
WINDOW_CAPTION = 'Platformer'
WINDOW_ICON = pygame.image.load(
    os.path.join('images', 'icon.png'))
BACKGROUND_COLOR = (200, 200, 155)
FPS = 60
JUMP_COUNT = 10
