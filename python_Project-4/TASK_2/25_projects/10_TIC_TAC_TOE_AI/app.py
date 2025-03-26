import random

board = [" "]*9
players = ["X", "O"]

def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6: print("-----------")

def check_win(player):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(all(board[i] == player for i in combo) for combo in wins)

def minimax(is_max):
    if check_win("O"): return 1
    if check_win("X"): return -1
    if " " not in board: return 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = players[is_max]
            scores.append(minimax(not is_max))
            board[i] = " "
    return max(scores) if is_max else min(scores)

def ai_move():
    best_score, best_move = -2, None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score, best_move = score, i
    board[best_move] = "O"

while True:
    print_board()
    if " " not in board or check_win("O") or check_win("X"): break
    move = int(input("Your move (0-8): "))
    if board[move] == " ": board[move] = "X"
    ai_move()