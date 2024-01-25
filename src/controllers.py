"""
Game controllers
© Andboogl, 2024
"""


import pygame
import settings
import objects


class Controllers:
    """Controllers"""
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
        """Players movement and drawing"""
        self.__player.draw()
        self.__player2.draw()

        # Moving players
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.__player.move('left', self.__blocks)

        if keys[pygame.K_d]:
            self.__player.move('right', self.__blocks)

        if keys[pygame.K_LEFT]:
            self.__player2.move('left', self.__blocks)

        if keys[pygame.K_RIGHT]:
            self.__player2.move('right', self.__blocks)

        # Jumping and moving down for player 1
        if not self.__player.is_jumping:
            self.__player.move('down', self.__blocks)

            if keys[pygame.K_SPACE]:
                self.__player.is_jumping = True

        else:
            if self.__player.jump_count >= -settings.JUMP_COUNT:
                if self.__player.jump_count > 0:
                    self.__player.move(
                        'top',
                        self.__blocks,
                        10)

                else:
                    self.__player.move(
                        'down', 
                        self.__blocks,
                        10)

                self.__player.jump_count -= 1

            else:
                self.__player.is_jumping = False
                self.__player.jump_count = settings.JUMP_COUNT

        # Jumping and moving down for player 2
        if not self.__player2.is_jumping:
            self.__player2.move('down', self.__blocks)

            if keys[pygame.K_UP]:
                self.__player2.is_jumping = True

        else:
            if self.__player2.jump_count >= -settings.JUMP_COUNT:
                if self.__player2.jump_count > 0:
                    self.__player2.move(
                        'top',
                        self.__blocks,
                        10)

                else:
                    self.__player2.move(
                        'down', 
                        self.__blocks,
                        10)

                self.__player2.jump_count -= 1

            else:
                self.__player2.is_jumping = False
                self.__player2.jump_count = settings.JUMP_COUNT
