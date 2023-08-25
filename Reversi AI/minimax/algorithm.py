from copy import deepcopy
import pygame

from reversi.constants import WHITE, BLACK


def minimax(game, depth, alpha, beta, max_player, window=None):
    if (depth == 0) or (game.get_winner() != False):
        return game.evaluate(), game.board

    if max_player == WHITE:
        max_eval = float('-inf')
        best_move = None

        for move in game.get_valid_moves(WHITE):
            new_game = simulate_move(game, move, WHITE)

            if window != None:
                new_game.draw(window)
                pygame.time.delay(100)

            evaluation = minimax(new_game, depth-1, alpha, beta, WHITE)[0]
            max_eval = max(max_eval, evaluation)
            alpha = max(alpha, evaluation)

            if beta <= alpha:
                break

            if max_eval == evaluation:
                best_move = move

        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None

        for move in game.get_valid_moves(BLACK):
            new_game = simulate_move(game, move, BLACK) 

            if window != None:
                new_game.draw(window)
                pygame.time.delay(100)

            evaluation = minimax(new_game, depth-1, alpha, beta, BLACK)[0]
            min_eval = min(min_eval, evaluation)
            beta = min(beta, evaluation)

            if beta <= alpha:
                break

            if min_eval == evaluation:
                best_move = move

        return min_eval, best_move


def simulate_move(game, move, player):
    new_game = deepcopy(game)
    new_game.place_piece(move[0], move[1], player)
    return new_game
