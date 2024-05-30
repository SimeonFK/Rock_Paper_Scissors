import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_wins = 0
computer_wins = 0
draws = 0

player_move = input('Choose - [r]ock  [p]aper  [s]cissors: ')

while True:

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    elif player_move == 'Exit':
        print('You exited! Hope we meet again.')
        break
    else:
        raise SystemExit("Invalid input! Don't input something that you shouldn't !!! - Try again later...")

    computer_random_number = random.randint(1, 3)
    computer_move = ''

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors
    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or\
        (player_move == scissors and computer_move == paper) or \
        (player_move == paper and computer_move == rock):
        player_wins += 1
        print(f'You win! - Wins({player_wins})')
        print()

    elif player_move == computer_move:
        draws += 1
        print(f'Draw! - Draws({draws})')
        print()

    else:
        computer_wins += 1
        print(f'You lose! - Loses({computer_wins})')
        print()

    player_move = input('Choose - [r]ock  [p]aper  [s]cissors: ')

