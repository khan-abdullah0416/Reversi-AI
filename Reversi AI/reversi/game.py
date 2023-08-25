import pygame

from .constants import WIDTH, HEIGHT, ROWS, COLS, SQUARE_SIZE, WHITE, BLACK, GREEN, BLUE


def get_row_col(position):
    x, y = position
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE

    return row, col


class Game:
    def __init__(self):
        self.set_up_board()
        self.player_turn = BLACK
        self.turn_passed = False
        self.if_winner = False

    def reset(self):
        self.__init__()

    def set_up_board(self):
        self.board = [
            [None for _ in range(COLS)],
            [None for _ in range(COLS)],
            [None for _ in range(COLS)],
            [None, None, None, WHITE, BLACK, None, None, None],
            [None, None, None, BLACK, WHITE, None, None, None],
            [None for _ in range(COLS)],
            [None for _ in range(COLS)],
            [None for _ in range(COLS)]
        ]

    def clear_board(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]

    def get_board(self):
        return self.board

    def change_turn(self):
        if self.get_player_turn() == WHITE:
            self.player_turn = BLACK
        elif self.get_player_turn() == BLACK:
            self.player_turn = WHITE

    def get_player_turn(self):
        return self.player_turn

    def get_score(self):
        white_score = 0
        black_score = 0

        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == WHITE:
                    white_score += 1
                elif self.board[row][col] == BLACK:
                    black_score += 1

        return white_score, black_score

    def get_winner(self):
        if self.if_winner == True:
            white_score, black_score = self.get_score()

            if white_score > black_score:
                return WHITE
            elif white_score < black_score:
                return BLACK
            else:
                return 0

        return False

    def draw(self, window):
        pygame.init()
        large_font = pygame.font.SysFont('turok.ttf', 55)
        small_font = pygame.font.SysFont('turok.ttf', 30)

        window.fill(GREEN)

        winner = self.get_winner()

        if winner == False:
            valid_moves = self.get_valid_moves(self.player_turn)

            for i in range(ROWS + 1):
                pygame.draw.rect(window, BLACK, pygame.Rect(
                    (i * SQUARE_SIZE) - 1, 0, 2, HEIGHT))
                pygame.draw.rect(window, BLACK, pygame.Rect(
                    0, (i * SQUARE_SIZE) - 1, WIDTH, 2))

            for row in range(ROWS):
                for col in range(COLS):
                    if self.board[row][col] == WHITE:
                        pygame.draw.circle(window, WHITE, [(
                            col * SQUARE_SIZE) + (SQUARE_SIZE // 2), (row * SQUARE_SIZE) + (SQUARE_SIZE // 2)], 40, 0)
                    elif self.board[row][col] == BLACK:
                        pygame.draw.circle(window, BLACK, [(
                            col * SQUARE_SIZE) + (SQUARE_SIZE // 2), (row * SQUARE_SIZE) + (SQUARE_SIZE // 2)], 40, 0)

                    if [row, col] in valid_moves:
                        pygame.draw.circle(window, WHITE, [(
                            col * SQUARE_SIZE) + (SQUARE_SIZE // 2), (row * SQUARE_SIZE) + (SQUARE_SIZE // 2)], 40, 1)

            mouse_row, mouse_col = get_row_col(pygame.mouse.get_pos())

            if [mouse_row, mouse_col] in valid_moves:
                pygame.draw.circle(window, BLUE, [(mouse_col * SQUARE_SIZE) + (
                    SQUARE_SIZE // 2), (mouse_row * SQUARE_SIZE) + (SQUARE_SIZE // 2)], 40, 1)

            if self.player_turn == WHITE:
                txtsurf = large_font.render('White', True, WHITE)
            elif self.player_turn == BLACK:
                txtsurf = large_font.render('Black', True, BLACK)

            window.blit(txtsurf, (310, 730))
        else:
            if winner == WHITE:
                txtsurf = large_font.render('White Wins', True, WHITE)
            elif winner == BLACK:
                txtsurf = large_font.render('Black Wins', True, BLACK)
            elif winner == 0:
                txtsurf = large_font.render('Draw', True, WHITE)

            window.blit(txtsurf, (250, 250))

        white_score, black_score = self.get_score()

        txtsurf = small_font.render('White: ' + str(white_score), True, WHITE)
        window.blit(txtsurf, (600, 725))

        txtsurf = small_font.render('Black: ' + str(black_score), True, BLACK)
        window.blit(txtsurf, (604, 750))

        pygame.display.update()

    def uld_flank(self, row, col, player) -> bool:
        # Upper Left Diagonal
        found_opp = False

        if (self.board[row][col] != None):
            return False

        if row > col:
            for i in range(1, col + 1):
                piece = self.board[row - i][col - i]

                if piece == None:
                    break
                elif (found_opp == False) and (piece == player):
                    break
                elif piece != player:
                    found_opp = True
                elif (found_opp == True) and (piece == player):
                    return True
        else:
            for i in range(1, row + 1):
                piece = self.board[row - i][col - i]

                if piece == None:
                    break
                elif (found_opp == False) and (piece == player):
                    break
                elif piece != player:
                    found_opp = True
                elif (found_opp == True) and (piece == player):
                    return True

        return False

    def lrd_flank(self, row, col, player) -> bool:
        # Lower Right Diagonal
        found_opp = False

        if (self.board[row][col] != None):
            return False

        if row > col:
            for i in range(1, ROWS - row):
                piece = self.board[row + i][col + i]

                if piece == None:
                    break
                elif (found_opp == False) and (piece == player):
                    break
                elif piece != player:
                    found_opp = True
                elif (found_opp == True) and (piece == player):
                    return True
        else:
            for i in range(1, COLS - col):
                piece = self.board[row + i][col + i]

                if piece == None:
                    break
                elif (found_opp == False) and (piece == player):
                    break
                elif piece != player:
                    found_opp = True
                elif (found_opp == True) and (piece == player):
                    return True

        return False

    def urd_flank(self, row, col, player) -> bool:
        # Upper Right Diagonal
        found_opp = False

        if (self.board[row][col] != None):
            return False

        if row + col > 7:
            for i in range(1, COLS - col):
                piece = self.board[row - i][col + i]

                if piece == None:
                    break
                elif (found_opp == False) and (piece == player):
                    break
                elif piece != player:
                    found_opp = True
                elif (found_opp == True) and (piece == player):
                    return True
        else:
            for i in range(1, row + 1):
                piece = self.board[row - i][col + i]

                if piece == None:
                    break
                elif (found_opp == False) and (piece == player):
                    break
                elif piece != player:
                    found_opp = True
                elif (found_opp == True) and (piece == player):
                    return True

        return False

    def lld_flank(self, row, col, player) -> bool:
        # Lower Left Diagonal
        found_opp = False

        if (self.board[row][col] != None):
            return False

        if row + col > 7:
            for i in range(1, ROWS - row):
                piece = self.board[row + i][col - i]

                if piece == None:
                    break
                elif (found_opp == False) and (piece == player):
                    break
                elif piece != player:
                    found_opp = True
                elif (found_opp == True) and (piece == player):
                    return True
        else:
            for i in range(1, col + 1):
                piece = self.board[row + i][col - i]

                if piece == None:
                    break
                elif (found_opp == False) and (piece == player):
                    break
                elif piece != player:
                    found_opp = True
                elif (found_opp == True) and (piece == player):
                    return True

        return False

    def uv_flank(self, row, col, player) -> bool:
        # Upper Vertical
        found_opp = False

        if (self.board[row][col] != None):
            return False

        for i in range(1, row + 1):
            piece = self.board[row - i][col]

            if piece == None:
                break
            elif (found_opp == False) and (piece == player):
                break
            elif piece != player:
                found_opp = True
            elif (found_opp == True) and (piece == player):
                return True

        return False

    def lv_flank(self, row, col, player) -> bool:
        # Lower Vertical
        found_opp = False

        if (self.board[row][col] != None):
            return False

        for i in range(1, ROWS - row):
            piece = self.board[row + i][col]

            if piece == None:
                break
            elif (found_opp == False) and (piece == player):
                break
            elif piece != player:
                found_opp = True
            elif (found_opp == True) and (piece == player):
                return True

        return False

    def lh_flank(self, row, col, player) -> bool:
        # Left Horizontal
        found_opp = False

        if (self.board[row][col] != None):
            return False

        for i in range(1, col + 1):
            piece = self.board[row][col - i]

            if piece == None:
                break
            elif (found_opp == False) and (piece == player):
                break
            elif piece != player:
                found_opp = True
            elif (found_opp == True) and (piece == player):
                return True

        return False

    def rh_flank(self, row, col, player) -> bool:
        # Right Horizontal
        found_opp = False

        if (self.board[row][col] != None):
            return False

        for i in range(1, COLS - col):
            piece = self.board[row][col + i]

            if piece == None:
                break
            elif (found_opp == False) and (piece == player):
                break
            elif piece != player:
                found_opp = True
            elif (found_opp == True) and (piece == player):
                return True

        return False

    def check_flanks(self, row, col, player) -> bool:
        # Upper Left Diagonal
        if self.uld_flank(row, col, player) == True:
            return True

        # Lower Right Diagonal
        if self.lrd_flank(row, col, player) == True:
            return True

        # Upper Right Diagonal
        if self.urd_flank(row, col, player) == True:
            return True

        # Lower Left Diagonal
        if self.lld_flank(row, col, player) == True:
            return True

        # Upper Vertical
        if self.uv_flank(row, col, player) == True:
            return True

        # Lower Vertical
        if self.lv_flank(row, col, player) == True:
            return True

        # Left Horizontal
        if self.lh_flank(row, col, player) == True:
            return True

        # Right Horizontal
        if self.rh_flank(row, col, player) == True:
            return True

        return False

    def get_valid_moves(self, player) -> list:
        valid_moves = []

        for row in range(ROWS):
            for col in range(COLS):
                if (self.board[row][col] != None) and (self.board[row][col] != player):

                    if row - 1 >= 0:
                        x = row - 1

                        if col - 1 >= 0:
                            y = col - 1

                            # Upper Left Diagonal
                            if ([x, y] not in valid_moves) and (self.check_flanks(x, y, player) == True):
                                valid_moves.append([x, y])

                        y = col

                        # Upper Vertical
                        if ([x, y] not in valid_moves) and (self.check_flanks(x, y, player) == True):
                            valid_moves.append([x, y])

                        if col + 1 < COLS:
                            y = col + 1

                            # Upper Right Diagonal
                            if ([x, y] not in valid_moves) and (self.check_flanks(x, y, player) == True):
                                valid_moves.append([x, y])

                    x = row

                    if col - 1 >= 0:
                        y = col - 1

                        # Left Horizontal
                        if ([x, y] not in valid_moves) and (self.check_flanks(x, y, player) == True):
                            valid_moves.append([x, y])

                    if col + 1 < COLS:
                        y = col + 1

                        # Right Horizontal
                        if ([x, y] not in valid_moves) and (self.check_flanks(x, y, player) == True):
                            valid_moves.append([x, y])

                    if row + 1 < ROWS:
                        x = row + 1

                        if col - 1 >= 0:
                            y = col - 1

                            # Lower Left Diagonal
                            if ([x, y] not in valid_moves) and (self.check_flanks(x, y, player) == True):
                                valid_moves.append([x, y])

                        y = col

                        # Lower Vertical
                        if ([x, y] not in valid_moves) and (self.check_flanks(x, y, player) == True):
                            valid_moves.append([x, y])

                        if col + 1 < COLS:
                            y = col + 1

                            # Lower Right Diagonal
                            if ([x, y] not in valid_moves) and (self.check_flanks(x, y, player) == True):
                                valid_moves.append([x, y])

        return valid_moves

    def flip_pieces(self, row, col, player):
        # Upper Left Diagonal
        if self.uld_flank(row, col, player) == True:
            if row > col:
                for i in range(1, col + 1):
                    piece = self.board[row - i][col - i]

                    if piece != player:
                        self.board[row - i][col - i] = player
                    elif piece == player:
                        break
            else:
                for i in range(1, row + 1):
                    piece = self.board[row - i][col - i]

                    if piece != player:
                        self.board[row - i][col - i] = player
                    elif piece == player:
                        break

        # Lower Right Diagonal
        if self.lrd_flank(row, col, player) == True:
            if row > col:
                for i in range(1, ROWS - row):
                    piece = self.board[row + i][col + i]

                    if piece != player:
                        self.board[row + i][col + i] = player
                    elif piece == player:
                        break
            else:
                for i in range(1, COLS - col):
                    piece = self.board[row + i][col + i]

                    if piece != player:
                        self.board[row + i][col + i] = player
                    elif piece == player:
                        break

        # Upper Right Diagonal
        if self.urd_flank(row, col, player) == True:
            if row + col > 7:
                for i in range(1, COLS - col):
                    piece = self.board[row - i][col + i]

                    if piece != player:
                        self.board[row - i][col + i] = player
                    elif piece == player:
                        break
            else:
                for i in range(1, row + 1):
                    piece = self.board[row - i][col + i]

                    if piece != player:
                        self.board[row - i][col + i] = player
                    elif piece == player:
                        break

        # Lower Left Diagonal
        if self.lld_flank(row, col, player) == True:
            if row + col > 7:
                for i in range(1, ROWS - row):
                    piece = self.board[row + i][col - i]

                    if piece != player:
                        self.board[row + i][col - i] = player
                    elif piece == player:
                        break
            else:
                for i in range(1, col + 1):
                    piece = self.board[row + i][col - i]

                    if piece != player:
                        self.board[row + i][col - i] = player
                    elif piece == player:
                        break

        # Upper Vertical
        if self.uv_flank(row, col, player) == True:
            for i in range(1, row + 1):
                piece = self.board[row - i][col]

                if piece != player:
                    self.board[row - i][col] = player
                elif piece == player:
                    break

        # Lower Vertical
        if self.lv_flank(row, col, player) == True:
            for i in range(1, ROWS - row):
                piece = self.board[row + i][col]

                if piece != player:
                    self.board[row + i][col] = player
                elif piece == player:
                    break

        # Left Horizontal
        if self.lh_flank(row, col, player) == True:
            for i in range(1, col + 1):
                piece = self.board[row][col - i]

                if piece != player:
                    self.board[row][col - i] = player
                elif piece == player:
                    break

        # Right Horizontal
        if self.rh_flank(row, col, player) == True:
            for i in range(1, COLS - col):
                piece = self.board[row][col + i]

                if piece != player:
                    self.board[row][col + i] = player
                elif piece == player:
                    break

    def place_piece(self, row, col, player):
        if [row, col] in self.get_valid_moves(player):
            self.flip_pieces(row, col, player)
            self.board[row][col] = player
            self.change_turn()
            self.turn_passed = False

            if self.get_valid_moves(self.get_player_turn()) == []:
                self.change_turn()
                self.turn_passed = True

                if self.get_valid_moves(self.get_player_turn()) == []:
                    self.if_winner = True

    def evaluate(self):
        white_score, black_score = self.get_score()
        return white_score - black_score
