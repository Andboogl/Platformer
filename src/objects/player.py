"""
Player
© Andboogl, 2024
"""


import pygame
import settings


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

    def move(self, where: str, blocks_list: list, speed: int = None) -> None:
        """Move player"""
        speed = speed if speed else self.__speed

        if where == 'left':
            new_coordinate = self.__x - speed

            for block in blocks_list:
                if block.image_rect.colliderect(self.__image_rect):
                    if self.__y + self.__image_rect.height / 2 - 5\
                        <= block.y + block.image_rect.height and\
                        self.__y + self.__image_rect.height / 2 + 5 >= block.y:
                        if not self.__x - 6 < block.x:
                            break

            else:
                if new_coordinate >= 0:
                    self.__x -= speed

        elif where == 'right':
            new_coordinate = self.__x + self.__image_rect.width + speed

            for block in blocks_list:
                if block.image_rect.colliderect(self.__image_rect):
                    if self.__y + self.__image_rect.height / 2 - 5\
                        <= block.y + block.image_rect.height and\
                        self.__y + self.__image_rect.height / 2 + 5 >= block.y:
                        if not self.__x + 6 > block.x + block.image_rect.width:
                            break

            else:
                if new_coordinate <= settings.WINDOW_SIZE[0]:
                    self.__x += speed

        elif where == 'top':
            new_coordinate = self.__y - speed

            for block in blocks_list:
                if block.image_rect.colliderect(self.__image_rect):
                    if not new_coordinate <= block.y - block.image_rect.height / 2:
                        break

            else:
                if new_coordinate > 0:
                    self.__y -= speed

        elif where == 'down':
            new_coordinate = self.__y + self.__image_rect.height + speed

            for block in blocks_list:
                if block.image_rect.colliderect(self.__image_rect):
                    if new_coordinate >= block.y:
                        break

            else:
                if new_coordinate <= settings.WINDOW_SIZE[1]:
                    self.__y += speed

        else:
            raise ValueError(f'{where} not recognized')

        # Updating player image
        self.__image_rect = pygame.rect.Rect(
            self.__x, self.__y,
            self.__size[0],
            self.__size[1])

    def draw(self) -> None:
        """Draw rect on the screen"""
        pygame.draw.rect(self.__screen,
                         self.__color,
                         self.__image_rect)
