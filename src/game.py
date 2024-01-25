"""
Game
© Andboogl, 2024
"""


import pygame
import settings
from controllers import Controllers


class Game:
    """Game"""
    def __init__(self) -> None:
        """Initializing class"""
        self.__screen = pygame.display.set_mode(settings.WINDOW_SIZE)
        self.__clock = pygame.time.Clock()
        pygame.display.set_caption(settings.WINDOW_CAPTION)
        pygame.display.set_icon(settings.WINDOW_ICON)

        self.__controllers = Controllers(self, self.__screen)

    def mainloop(self) -> None:
        """Game mainloop"""
        while True:
            self.__screen.fill(settings.BACKGROUND_COLOR)

            self.__controllers.players()
            self.__controllers.blocks()
            self.__controllers.enemies()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)

            self.__clock.tick(settings.FPS)
            pygame.display.update()
