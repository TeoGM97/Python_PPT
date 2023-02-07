#Rock Paper Scissors Game

user_option = input('Rock, Papaer o Scissors? => ')
user_option = user_option.lower
pc_option = 'rock'

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