"""
Player controller
© Andboogl, 2024
"""


import os
import random
import pygame
import settings


def players(player1, player2, blocks: list, bonus_list: list) -> tuple:
    """Players movement and drawing"""
    player1.draw()
    player2.draw()

    # Moving players
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player1.move('left', blocks)

    if keys[pygame.K_d]:
        player1.move('right', blocks)

    if keys[pygame.K_LEFT]:
        player2.move('left', blocks)

    if keys[pygame.K_RIGHT]:
        player2.move('right', blocks)

    # Bonus drawing and checking
    for bonus in bonus_list:
        bonus.draw()

        if bonus.image_rect.colliderect(player1.image_rect):
            bonus_action = random.choice([1, 2])

            if bonus_action == 1:
                player1.speed += settings.PLAYER_ACCELERATION

            else:
                player1.base_jump_count += settings.PLAYER_JUMP_ACCELERATION

            bonus_list.remove(bonus)
            pygame.mixer.Sound(os.path.join(
                'sounds', 'bonus.mp3')).play()

        if bonus.image_rect.colliderect(player2.image_rect):
            bonus_action = random.choice([1, 2])

            if bonus_action == 1:
                player2.speed += settings.PLAYER_ACCELERATION

            else:
                player2.base_jump_count += settings.PLAYER_JUMP_ACCELERATION

            bonus_list.remove(bonus)
            pygame.mixer.Sound(os.path.join(
                'sounds', 'bonus.mp3')).play()

    # Jumping and moving down for player 1
    if not player1.is_jumping:
        player1.move('down', blocks, settings.GRAVITATION)

        if keys[pygame.K_SPACE]:
            player1.is_jumping = True
            pygame.mixer.Sound(os.path.join(
                'sounds', 'jump.mp3')).play()

    else:
        if player1.jump_count >= -player1.base_jump_count:
            if player1.jump_count > 0:
                player1.move(
                    'top',
                    blocks,
                    10)

            else:
                player1.move(
                    'down', 
                    blocks,
                    settings.GRAVITATION)

            player1.jump_count -= 1

        else:
            player1.is_jumping = False
            player1.jump_count = player1.base_jump_count

    # Jumping and moving down for player 2
    if not player2.is_jumping:
        player2.move('down', blocks, settings.GRAVITATION)

        if keys[pygame.K_UP]:
            player2.is_jumping = True
            pygame.mixer.Sound(os.path.join(
                'sounds', 'jump.mp3')).play()

    else:
        if player2.jump_count >= -player2.base_jump_count:
            if player2.jump_count > 0:
                player2.move(
                    'top',
                    blocks,
                    10)

            else:
                player2.move(
                    'down', 
                    blocks,
                    10)

            player2.jump_count -= 1

        else:
            player2.is_jumping = False
            player2.jump_count = player2.base_jump_count

    return (bonus_list,)
