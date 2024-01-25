"""
Bonus
© Andboogl, 2024
"""


import pygame


class Bonus:
    """Bonus"""
    def __init__(self, screen, x: int, y: int) -> None:
        """Initializing class"""
        self.__screen = screen
        self.__x = x
        self.__y = y
        self.__color = (44, 255, 44)
        self.__size = (25, 25)

        # Bonus image
        self.__image_rect = pygame.rect.Rect(self.__x, 
                                             self.__y,
                                             self.__size[0],
                                             self.__size[1])

    @property
    def image_rect(self) -> pygame.rect.Rect:
        """Get bonus image rect"""
        return self.__image_rect

    def draw(self) -> None:
        """Draw bonus"""
        pygame.draw.rect(self.__screen,
                         self.__color,
                         self.__image_rect)
