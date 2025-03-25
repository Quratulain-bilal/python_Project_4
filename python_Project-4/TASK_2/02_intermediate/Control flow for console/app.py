
import random

print("Welcome to the High-Low Game!\n----------------------------")

computer = random.randint(1, 10)
chances = 10

for round in range(1, chances + 1):
    user_guess = int(input(f'Round {round} - Enter your guess (1-10): '))

    if user_guess > computer:
        print("Your number is higher than the computer's.")
    elif user_guess < computer:
        print("Your number is lower than the computer's.")
    else:
        print(f'You guessed it! The computer\'s number was {computer}.')
        print(f'Your score is {5 if round == 1 else 2 if round <= chances // 2 else 1}.')
        break
else:
    print(f'Game over! The correct number was {computer}. Better luck next time!')
