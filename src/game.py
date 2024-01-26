"""
Game
© Andboogl, 2024
"""


import pygame
import settings
from controller import Controller


class Game:
    """Game"""
    __players_data_show = False

    def __init__(self) -> None:
        """Initializing class"""
        pygame.init()
        self.__screen = pygame.display.set_mode(settings.WINDOW_SIZE)
        self.__clock = pygame.time.Clock()
        pygame.display.set_caption(settings.WINDOW_CAPTION)
        pygame.display.set_icon(settings.WINDOW_ICON)

        self.__controllers = Controller(self, self.__screen)

    def mainloop(self) -> None:
        """Game mainloop"""
        while True:
            self.__screen.fill(settings.BACKGROUND_COLOR)

            self.__controllers.players()
            self.__controllers.blocks()
            self.__controllers.enemies()

            if self.__players_data_show:
                self.__controllers.players_data()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.__init__()

                    elif event.key == pygame.K_TAB:
                        self.__players_data_show = False if self.__players_data_show else True

            self.__clock.tick(settings.FPS)
            pygame.display.update()
