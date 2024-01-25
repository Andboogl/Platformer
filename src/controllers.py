"""
Game controllers
© Andboogl, 2024
"""


import pygame
import settings


class Controllers:
    """Controllers"""
    def __init__(self, game, screen,
                 players: list,
                 blocks: list,
                 enemies: list) -> None:
        """Initializing class"""
        self.__game = game
        self.__screen = screen
        self.__player = players[0]
        self.__player2 = players[1]
        self.__blocks = blocks
        self.__enemies = enemies

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

    def players_movement(self) -> None:
        """Player movement"""
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
