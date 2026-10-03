board = [""] * 9

def display_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(player):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def tic_tac_toe():
    current_player = "X"
    for turn in range(9):
        display_board()
        print(f"Player {current_player}'s turn")
        while True:
            try:
                position = int(input("Enter position (1-9): ")) - 1
                if position < 0 or position > 8:
                    print("Please enter a number between 1 and 9.")
                elif board[position] != "":
                    print("Position already occupied. Try again.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")
        
        board[position] = current_player
        
        if check_winner(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            return
        
        current_player = "O" if current_player == "X" else "X"
        
    display_board()
    print("The game is a draw!")

tic_tac_toe()
