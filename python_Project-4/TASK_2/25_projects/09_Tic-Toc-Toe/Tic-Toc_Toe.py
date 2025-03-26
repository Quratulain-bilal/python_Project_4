import os

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    clear_output()  # Clears cell output between moves
    print(f"""
     {board[0]} | {board[1]} | {board[2]}
    -----------
     {board[3]} | {board[4]} | {board[5]}
    -----------
     {board[6]} | {board[7]} | {board[8]}
    """)

def play_game():
    board = [" "]*9
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Get valid move
        while True:
            try:
                move = int(input("Enter position (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == " ":
                    break
                print("Invalid move! Try again.")
            except:
                print("Please enter a number 1-9!")

        # Make move
        board[move] = current_player

        # Check for winner
        winning_combos = [
            [0,1,2], [3,4,5], [6,7,8],  # rows
            [0,3,6], [1,4,7], [2,5,8],    # columns
            [0,4,8], [2,4,6]              # diagonals
        ]

        for combo in winning_combos:
            if all(board[i] == current_player for i in combo):
                print_board(board)
                print(f"Player {current_player} wins!")
                return

        # Check for tie
        if " " not in board:
            print_board(board)
            print("It's a tie!")
            return

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()