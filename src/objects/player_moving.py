"""
Player moving
© Andboogl, 2024
"""


import pygame
import settings


def move_player(self, where: str, blocks_list: list, speed: int = None) -> None:
    """Move player"""
    speed = speed if speed else self.speed
    x = self.x
    y = self.y

    if where == 'left':
        new_coordinate = self.x - speed

        for block in blocks_list:
            if block.image_rect.colliderect(self.image_rect):
                if self.y + self.image_rect.height / 2 + 8 >= block.y and\
                    self.y + self.image_rect.height / 2 - 8 <= block.y +\
                    block.image_rect.height:
                    if new_coordinate >= block.x:
                        break

        else:
            if new_coordinate >= 0:
                x -= speed

            else:
                x = 0

    elif where == 'right':
        new_coordinate = self.x + self.image_rect.width + speed

        for block in blocks_list:
            if block.image_rect.colliderect(self.image_rect):
                if self.y + self.image_rect.height / 2 + 8 >= block.y and\
                    self.y + self.image_rect.height / 2 - 8 <= block.y +\
                    block.image_rect.height:
                    if new_coordinate >= block.x:
                        break

        else:
            if new_coordinate <= settings.WINDOW_SIZE[0]:
                x += speed

            else:
                x = settings.WINDOW_SIZE[0] -self.image_rect.width

    elif where == 'top':
        new_coordinate = self.y - speed

        for block in blocks_list:
            if block.image_rect.colliderect(self.image_rect):
                if not self.y <= block.y:
                    break

        else:
            if new_coordinate > 0:
                y -= speed

            else:
                y = 0

    elif where == 'down':
        new_coordinate = self.y + self.image_rect.height + speed

        for block in blocks_list:
            if self.image_rect.colliderect(block.image_rect):
                break

        else:
            if new_coordinate <= settings.WINDOW_SIZE[1]:
                y += speed

            else:
                y = settings.WINDOW_SIZE[1] - self.image_rect.height

    else:
        raise ValueError(f'{where} not recognized')

    # Updating player image
    result = pygame.rect.Rect(
        self.x, self.y,
        self.size[0],
        self.size[1])

    return (result, x, y)
