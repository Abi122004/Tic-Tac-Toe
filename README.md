# Tic-Tac-Toe
Tic Tac Toe Game
Description
This project is a simple implementation of the classic Tic Tac Toe game in Python. It allows two players to play the game on a 3x3 grid. The game includes features such as checking for a win or a draw and validating user input.

Features
Display the game board with cell coordinates for easy reference.
Allow two players to take turns and make moves.
Validate player input to ensure moves are made in empty cells within the grid.
Check for a win or a draw after each move.
Display the game board and announce the winner or if the game is a draw.
Requirements
Python 3.x

Code Explanation
print_board(board)
This function displays the current state of the game board. It shows the cell coordinates for empty cells and the players' moves.

check_win(board, player)
This function checks if the specified player has won the game by forming a horizontal, vertical, or diagonal line.

check_draw(board)
This function checks if the game has ended in a draw, meaning all cells are filled, and there is no winner.

get_valid_input(board)
This function prompts the current player to enter their move. It ensures that the input is valid (numbers 1-3) and that the selected cell is empty.

tic_tac_toe()
This function is the main game loop. It initializes the game board, alternates between players, checks for a win or a draw, and displays the game board after each move.

Contact
For any questions or suggestions, feel free to contact me at abishek122004@gmail.com
