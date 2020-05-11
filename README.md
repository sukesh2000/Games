# Tic - Tac - Toe
To play this game:
1. You'll need to choose Player1's marker either, 'X' or 'O', Player2's(in dual player version) or Computer's(in single player version) marker will be decided automatically. 
2. You'll need to give confirmation to start the game.
3. After the game starts, you'll need to place the marker in the given layout, you could use your num-pad since the layout of the board is set according to the num-pad of the keyboard:
                                                                   |   |
                                                                 7 | 8 | 9
                                                                   |   |
                                                                ---+---+--
                                                                   |   |
                                                                 4 | 5 | 6
                                                                   |   |
                                                                ---+---+--
                                                                   |   |
                                                                 1 | 2 | 3
                                                                   |   |
4. Once the game is over you'll have two options, either to quit or replay.
5. Remaining instructions are inside the game.

The difference between two versions:
1. In v1.0, to decide who's going to play next, I've implemented one extra function viz., turn_play(t).
2. In v2.0, that function isn't present, instead of that I've used if...else conditional statements in the main function block itself to decide next player's turn.
