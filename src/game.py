"""
Game
© Andboogl, 2024
"""


import pygame
import settings
import objects
from controllers import Controllers


class Game:
    """Game"""
    def __init__(self) -> None:
        """Initializing class"""
        self.__screen = pygame.display.set_mode(settings.WINDOW_SIZE)
        self.__clock = pygame.time.Clock()
        pygame.display.set_caption(settings.WINDOW_CAPTION)
        pygame.display.set_icon(settings.WINDOW_ICON)

        # Game objects
        self.__player = objects.Player(self.__screen, 100, 500, (155, 155, 200))
        self.__player2 = objects.Player(self.__screen, 100, 500, (100, 255, 200))
        self.__blocks = [
            objects.Block(self.__screen, 41, 709),
            objects.Block(self.__screen, 351, 584),
            objects.Block(self.__screen, 688, 729),
            objects.Block(self.__screen, 895, 584),
            objects.Block(self.__screen, 665, 366),
            objects.Block(self.__screen, 41, 356),
            objects.Block(self.__screen, 394, 134),
            objects.Block(self.__screen, 959, 227),
        ]
        self.__enemies = [
            objects.Enemy(self.__screen, 751, 653),
            objects.Enemy(self.__screen, 1006, 341),
            objects.Enemy(self.__screen, 413, 226),
            objects.Enemy(self.__screen, 53, 297),
            objects.Enemy(self.__screen, 923, 49),
        ]
        self.__controllers = Controllers(self, self.__screen,
                                         [self.__player, self.__player2],
                                         self.__blocks,
                                         self.__enemies)

    def mainloop(self) -> None:
        """Game mainloop"""
        while True:
            self.__screen.fill(settings.BACKGROUND_COLOR)

            self.__controllers.blocks()
            self.__controllers.enemies()
            self.__controllers.players_movement()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)

            self.__clock.tick(settings.FPS)
            pygame.display.update()
