"""
Game controller
© Andboogl, 2024
"""


import objects
from .player import players


class Controller:
    """Main controller"""
    def __init__(self, game, screen) -> None:
        """Initializing class"""
        self.__game = game
        self.__screen = screen

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
        self.__bonus_list = [
            objects.Bonus(self.__screen, 103, 109),
            objects.Bonus(self.__screen, 538, 263),
            objects.Bonus(self.__screen, 763, 507),
            ]

    def blocks(self) -> None:
        """Drawing blocks"""
        for block in self.__blocks:
            block.draw()

    def enemies(self) -> None:
        """Checking for player die and drawing enemies"""
        for enemy in self.__enemies:
            enemy.draw()

            # Checking for die
            if self.__player.image_rect.colliderect(enemy.image_rect) or\
                self.__player2.image_rect.colliderect(enemy.image_rect):
                self.__game.__init__()

    def players(self) -> None:
        """Players controller"""
        result = players(self.__player, self.__player2, self.__blocks, self.__bonus_list)
        self.__bonus_list = result[0]
