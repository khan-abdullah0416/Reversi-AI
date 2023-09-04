# Reversi (Othello) AI

[Reversi](https://en.wikipedia.org/wiki/Reversi) is a strategy board game for two players, played on an 8×8 uncheckered board.

There are sixty-four identical game pieces called disks, which are light on one side and dark on the other. Players take turns placing disks on the board with their assigned color facing up. During a play, any disks of the opponent's color that are in a straight line and bounded by the disk just placed and another disk of the current player's color are turned over to the current player's color. The objective of the game is to have the majority of disks turned to display one's color when the last playable empty square is filled.

![Reversi Board in Pygame](/static/reversi-board.png)

## Playing the game

White squares indicte legal moves to place your disks, while a circle highlighted in blue indictes the current square selected.

The score and the which player's turn it is, is displayed at the bottom of the window.

When a player wins the game the game is paused for 3 - 5 seconds and then starts again.
