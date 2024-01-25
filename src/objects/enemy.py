"""
Enemy
© Andboogl, 2024
"""


import pygame


class Enemy:
    """Enemy"""
    def __init__(self, screen, x: int, y: int) -> None:
        """Initializing class"""
        self.__screen = screen
        self.__x = x
        self.__y = y
        self.__size = (50, 50)
        self.__color = (255, 20, 20)

        # Enemy image
        self.__image_rect = pygame.rect.Rect(
            self.__x, self.__y,
            self.__size[0],
            self.__size[1])

    @property
    def image_rect(self) -> pygame.rect.Rect:
        """Get enemy image rect"""
        return self.__image_rect

    def draw(self) -> None:
        """Draw enemy"""
        pygame.draw.rect(
            self.__screen, self.__color,
            self.__image_rect)
