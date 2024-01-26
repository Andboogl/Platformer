"""
Players data
© Andboogl, 2024
"""


import os
import pygame



def draw_text(screen, text: str, y: int) -> None:
    """Draw text"""
    text_color = (0, 0, 0)

    text_obj = pygame.font.Font(os.path.join(
        'fonts',
        'Montserrat-Bold.ttf')).render(
            text,
            True,
            text_color)
    screen.blit(text_obj, (10, y))


def players_data(screen, player1, player2) -> None:
    """Players data"""
    # Player1 data
    player1_data_text = f'player1.x = {player1.x}    '\
    f'player1.y = {player1.y}    '\
    f'player1.speed = {player1.speed}    '\
    f'player1.base_jump_count = {player1.base_jump_count}    '\
    f'player1.jump_count = {player1.jump_count}    player1.is_jumpi'\
    f'ng = {player1.is_jumping}'
    draw_text(screen, player1_data_text, 10)

    # Player2 data
    player2_data_text = f'player2.x = {player2.x}    '\
    f'player2.y = {player2.y}    '\
    f'player2.speed = {player2.speed}    '\
    f'player2.base_jump_count = {player2.base_jump_count}    '\
    f'player2.jump_count = {player2.jump_count}    player2.is_jumpi'\
    f'ng = {player2.is_jumping}'
    draw_text(screen, player2_data_text, 30)

    # Copyright
    draw_text(screen, '© Andboogl, 2024', 50)
    draw_text(screen, 'All rights reserved', 70)
