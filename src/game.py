"""
Game
© Andboogl, 2024
"""


import pygame
import settings
import objects


class Game:
    """Game"""
    def __init__(self) -> None:
        """Initializing class"""
        self.__screen = pygame.display.set_mode(settings.WINDOW_SIZE)
        self.__clock = pygame.time.Clock()
        pygame.display.set_caption(settings.WINDOW_CAPTION)
        pygame.display.set_icon(settings.WINDOW_ICON)

        # Game objects
        self.__player = objects.Player(self.__screen, 100, 0)
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

    def mainloop(self) -> None:
        """Game mainloop"""
        while True:
            self.__screen.fill(settings.BACKGROUND_COLOR)
            self.__player.draw()

            # Drawing block
            for block in self.__blocks:
                block.draw()

            # Moving player
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.__player.move('left', self.__blocks)

            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.__player.move('right', self.__blocks)

            # Jumping and moving down
            if not self.__player.is_jumping:
                self.__player.move('down', self.__blocks)

                if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                    self.__player.is_jumping = True

            else:
                if self.__player.jump_count >= -settings.JUMP_COUNT:
                    if self.__player.jump_count > 0:
                        self.__player.move(
                            'top',
                            self.__blocks,
                            15)

                    else:
                        self.__player.move(
                            'down', 
                            self.__blocks,
                            10)

                    self.__player.jump_count -= 1

                else:
                    self.__player.is_jumping = False
                    self.__player.jump_count = settings.JUMP_COUNT

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)

            self.__clock.tick(settings.FPS)
            pygame.display.update()
