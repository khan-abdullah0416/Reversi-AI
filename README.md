# Reversi (Othello) AI

[Reversi](https://en.wikipedia.org/wiki/Reversi) is a strategy board game for two players, played on an 8×8 uncheckered board.

There are sixty-four identical game pieces called disks, which are light on one side and dark on the other. Players take turns placing disks on the board with their assigned color facing up. During a play, any disks of the opponent's color that are in a straight line and bounded by the disk just placed and another disk of the current player's color are turned over to the current player's color. The objective of the game is to have the majority of disks turned to display one's color when the last playable empty square is filled.

![Reversi Board in Pygame](/static/reversi-board.png)

## Playing the game

White squares indicte legal moves to place your disks, while a circle highlighted in blue indictes the current square selected.

The score and the which player's turn it is, is displayed at the bottom of the window.

When a player wins the game the game is paused for 3 - 5 seconds and then starts again.

## Making your own board

It is possible to use the board as a module. I would recommend anyone who wants to make their own board to first inherit the `Board` class and then override the `draw` function.

### Board Methods

`reset()`

Reinitialises the board so that a new game can be played.

`set_up_board()`

Resets the board to its opening state.

`clear_board()`

Clears the board

`get_board`

Return the board the current game has. This is a 2d list.

`change_turn()`

Changes the player's turn from black to white or white to black.

`get_player_turn()`

Returns the current players turn.

`get_score()`

Return black and white's score. The score is based on the number of black or white pieces on the board.

`get_winner()`

Return if black or white won the game. If is it a draw return `0` and if there is no winner return `False`.

`draw(window)`

Draws the board and pieces on a pygame window.

`direction_flank(row, col, player)`

Checks if a flank occurs if a piece of color `player` was placed on row `row` and column `col` and returns either `True` or `False`.

Directions available:

uld - Upper Left Diagonal
lrd - Lower Right Diagonal
urd - Upper Right Diagonal
lld - Lower Left Diagonal
uv - Upper Vertical
lv - Lower Vertical
lh - Left Horizontal
rh- Right Horizontal

`check_flanks(row, col, player) -> bool`

Checks if a flank exists for a piece of color `player` on row `row` and column `col` and then return either `True` or `False`.

`get_valid_moves(player) ->`

Returns a list of valid moves for a player of color `player`.

`flip_pieces(row, col, player)`

Flips pieces that will be flanked when a piece of color `player` on row `row` and column `col` will be player on the board.

`places_piece(row, col, player)`

Places a piece of color `player` on row `row` and column `col` on the board.

`evaluate()`

Returns a score used to evaluate the board. Used by an external minimax algorithm to determine the best moves.
