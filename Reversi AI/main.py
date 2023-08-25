import pygame

from reversi.game import Game, get_row_col
from reversi.constants import WIDTH, HEIGHT, WHITE, BLACK
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT + 60))
pygame.display.set_caption('Reversi')


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game()

    while run:
        clock.tick(FPS)

        if game.get_winner() != False:
            game.reset()
            pygame.time.delay(3000)

        if game.get_player_turn() == WHITE:
            evaluation, move = minimax(game, 3, float('-inf'), float('inf'), WHITE, WIN)
            game.place_piece(move[0], move[1], WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, col = get_row_col(position)
                game.place_piece(row, col, game.get_player_turn())

        game.draw(WIN)

    pygame.quit()


if __name__ == '__main__':
    main()
