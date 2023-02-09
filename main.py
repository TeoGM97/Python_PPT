#Rock Paper Scissors Game
import random

#Tuple of options
options = ('rock', 'paper', 'scissors')

#Victories and rounds counters
pc_wins = 0
user_wins = 0
rounds = 1

#Loop to validate who wins 2 times
while pc_wins or user_wins < 2:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    print('  ')

    #Input user option
    user_option = input('Rock, Papaer o Scissors? => ')
    #Standarize input
    user_option = user_option.lower()

    if not user_option in options:
        print('  ')
        print('=> Are you okay? ')

    #Random selection of pc in options tuple
    pc_option = random.choice(options)

    #Show options in screen
    print('  ')
    print('User Option =>', user_option)
    print('PC Option =>', pc_option)
    print('  ')

    #Tie Validation
    if user_option == pc_option:
        print('Tie')
    #Game Logic (Win and Lose)
    #User uses Rock vs Scissors and Paper
    elif user_option == 'rock':
        if pc_option == 'scissors':
            print('  ')
            print('Rock defeat Scissors')
            print('  ')
            print('*' * 10)
            print('YOU WIN')
            print('*' * 10)
            print('  ')
            #+1 victory to user
            user_wins += 1
        else:
            print('  ')
            print('Paper defeat Rock')
            print('  ')
            print('*' * 10)
            print('GAME OVER')
            print('*' * 10)
            print('  ')
            #+1 victory to pc
            pc_wins += 1

    #User uses Paper vs Rock and Scissors
    elif user_option == 'paper':
        if pc_option == 'rock':
            print('  ')
            print('Paper defeat Rock')
            print('  ')
            print('*' * 10)
            print('YOU WIN')
            print('*' * 10)
            print('  ')
            #+1 victory to user
            user_wins += 1
        else:
            print('  ')
            print('Scissors defeat Paper')
            print('  ')
            print('*' * 10)
            print('GAME OVER')
            print('*' * 10)
            print('  ')
            #+1 victory to pc
            pc_wins += 1

    #User uses Scissors vs Paper and Rock
    elif user_option == 'scissors':
        if pc_option == 'paper':
            print('  ')
            print('Scissors defeat Paper')
            print('  ')
            print('*' * 10)
            print('YOU WIN')
            print('*' * 10)
            print('  ')
            #+1 victory to user
            user_wins += 1
        else:
            print('  ')
            print('Rock defeat Scissors')
            print('  ')
            print('*' * 10)
            print('GAME OVER')
            print('*' * 10)
            print('  ')
            #+1 victory to pc
            pc_wins += 1
    #Add 1 round to round counter
    rounds += 1