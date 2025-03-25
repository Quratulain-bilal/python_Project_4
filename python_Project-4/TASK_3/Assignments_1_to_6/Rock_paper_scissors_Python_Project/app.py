import random

def play():
    user = input("whats your choice?? \n'r' for rock, 'p' for paper and 's' for scissors\n")
    computer = random.choice(['r','p','s'])
    if computer == user:
        return 'tie'
    if is_win(user,computer):
        return ' You won! '
    return 'you lost!'
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())