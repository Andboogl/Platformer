"""
Player
© Andboogl, 2024
"""


import pygame
import settings
from .player_moving import move_player


class Player:
    """Player"""
    def __init__(self, screen, x: int, y: int, color: tuple) -> None:
        """Initializing class"""
        self.__screen = screen
        self.__x = x
        self.__y = y
        self.__color = color
        self.__size = (50, 50)
        self.__speed = 9
        self.__is_jumping = False
        self.__base_jump_count = settings.BASE_JUMP_COUNT
        self.__jump_count = settings.BASE_JUMP_COUNT

        # Player image
        self.__image_rect = pygame.rect.Rect(
            self.__x, self.__y,
            self.__size[0],
            self.__size[1])

    @property
    def base_jump_count(self) -> int:
        """Get base jump count"""
        return self.__base_jump_count

    @base_jump_count.setter
    def base_jump_count(self, value: int) -> int:
        """Get base jump count"""
        if isinstance(value, int):
            self.__base_jump_count = value

        else:
            raise TypeError(f'{value} must be integer')

    @property
    def speed(self) -> bool:
        """Get player speed"""
        return self.__speed

    @speed.setter
    def speed(self, value: int) -> None:
        """Change speed value"""
        if isinstance(value, int):
            self.__speed = value

        else:
            raise TypeError('Must be integer')

    @property
    def is_jumping(self) -> bool:
        """Get is jumping value"""
        return self.__is_jumping

    @is_jumping.setter
    def is_jumping(self, bool_: bool) -> None:
        """Set is jumping value"""
        if isinstance(bool_, bool):
            self.__is_jumping = bool_

        else:
            raise TypeError('Must be boolian')

    @property
    def jump_count(self) -> bool:
        """Get jump count value"""
        return self.__jump_count

    @jump_count.setter
    def jump_count(self, number: int) -> None:
        """Set jump count value"""
        if isinstance(number, int):
            self.__jump_count = number

        else:
            raise TypeError('Must be integer')

    @property
    def image_rect(self) -> pygame.rect.Rect:
        """Get player image rect"""
        return self.__image_rect

    @property
    def x(self) -> int:
        """Get player position on x"""
        return self.__x

    @property
    def y(self) -> int:
        """Get player position on y"""
        return self.__y

    @property
    def size(self) -> tuple:
        """Get player size"""
        return self.__size

    def move(self, where: str, blocks_list: list, speed: int = None) -> None:
        """Move player"""
        result = move_player(self,
                             where,
                             blocks_list,
                             speed if speed else None)
        self.__image_rect = result[0]
        self.__x = result[1]
        self.__y = result[2]

    def draw(self) -> None:
        """Draw rect on the screen"""
        pygame.draw.rect(self.__screen,
                         self.__color,
                         self.__image_rect)
