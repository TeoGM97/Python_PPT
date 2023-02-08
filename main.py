#Rock Paper Scissors Game
import random

#Tuple of options
options = ('rock', 'paper', 'scissors')

#Input user option
user_option = input('Rock, Papaer o Scissors? => ')
#Standarize input
user_option = user_option.lower()

if not user_option in options:
    print('Are you okay?')

#Random selection of pc in options tuple
pc_option = random.choice(options)

#Show options in screen
print('User Option =>', user_option)
print('PC Option =>', pc_option)


#Tie Validation
if user_option == pc_option:
    print('Tie')

#Game Logic (Win and Lose)
#User uses Rock vs Scissors and Paper
elif user_option == 'rock':
    if pc_option == 'scissors':
        print('Rock defeat Scissors')
        print('YOU WIN')
    else:
        print('Paper defeat Rock')
        print('GAME OVER')

#User uses Paper vs Rock and Scissors
elif user_option == 'paper':
    if pc_option == 'rock':
        print('Paper defeat Rock')
        print('YOU WIN')
    else:
        print('Scissors defeat Paper')
        print('GAME OVER')

#User uses Scissors vs Paper and Rock
elif user_option == 'scissors':
    if pc_option == 'paper':
        print('Scissors defeat Paper')
        print('YOU WIN')
    else:
        print('Rock defeat Scissors')
        print('GAME OVER')