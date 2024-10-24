# Hope Cano
# fire-water-earth.py aka rock-paper-scissors.py
# September 22, 2024
# CISW 24 

import random, time, sys

print('''Fire, Water, Earth, 
- Fire beats Earth.
- Earth beats Water.
- Water beats Fire. 
''')

# These variables keep track of the number of wins, losses, and ties. 
wins = 0
losses = 0
ties = 0

while True: #Main game Loop.
    while True: # Keep asking until player enters F, W, E, or Q.
        print('{} Wins, {} Losses, {} Ties'.format(wins, losses, ties))
        print('Enter your move: (F)ire (W)ater (E)arth or (Q)uit')
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if playerMove == 'F' or playerMove == 'W' or playerMove == 'E':
            break
        else:
            print('Type one of F, W, E, or Q.')

    # Display what the player chose:
    if playerMove == 'F':
        print('FIRE versus...')
        playerMove = 'FIRE'
    elif playerMove == 'W':
        print('WATER versus...')
        playerMove = 'WATER'
    elif playerMove == 'E':
        print('EARTH versus...')
        playerMove = 'EARTH'

    # Count to three with dramatic pauses:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'FIRE'
    elif randomNumber == 2:
        computerMove = 'WATER'
    elif randomNumber == 3:
        computerMove = 'EARTH'
    print(computerMove)
    time.sleep(0.5)

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It\'s a tie!')
        ties = ties + 1
    elif playerMove == 'FIRE' and computerMove == 'EARTH':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'EARTH' and computerMove == 'WATER':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'WATER' and computerMove == 'FIRE':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'FIRE' and computerMove == 'WATER':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'WATER' and computerMove == 'EARTH':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'EARTH' and computerMove == 'FIRE':
        print('You lose!')
        losses = losses + 1              