def print_board(board):
    print("--------------------------")
    for i, row in enumerate(board):
        row_display = []
        for j, cell in enumerate(row):
            if cell == " ":
                row_display.append(f"{i+1},{j+1}")
            else:
                row_display.append(cell)
        print(f" |  {'  |  '.join(row_display)} |  ")
        print("--------------------------")

def check_win(board, player):

    for i in range(3):
        if all(cell == player for cell in board[i]): 
            return True
        if all(board[j][i] == player for j in range(3)): 
            return True
    if all(board[i][i] == player for i in range(3)): 
        return True
    if all(board[i][2 - i] == player for i in range(3)):  
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_valid_input(board):
    while True:
        try:
            row = int(input("Enter the row (1, 2, 3): ")) - 1
            col = int(input("Enter the column (1, 2, 3): ")) - 1
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    return row, col
                else:
                    print("This cell is already taken. Choose another one.")
            else:
                print("Invalid input. Please enter numbers 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter numbers 1, 2, or 3.")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        row, col = get_valid_input(board)


        board[row][col] = current_player

       
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
