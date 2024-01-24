"""
Block
© Andboogl, 2024
"""


import pygame


class Block:
    """Block"""
    def __init__(self, screen, x: int, y: int) -> None:
        """Initializing class"""
        self.__screen = screen
        self.__x = x
        self.__y = y
        self.__color = (100, 100, 50)
        self.__size = (200, 20)

        # Block image
        self.__image_rect = pygame.rect.Rect(
            self.__x, self.__y,
            self.__size[0],
            self.__size[1])

    @property
    def x(self) -> int:
        """Get block position on x"""
        return self.__x

    @property
    def y(self) -> int:
        """Get block position on y"""
        return self.__y

    @property
    def image_rect(self) -> pygame.rect.Rect:
        """Get block image rect"""
        return self.__image_rect

    def draw(self) -> None:
        """Draw block"""
        pygame.draw.rect(
            self.__screen, self.__color,
            self.__image_rect)
