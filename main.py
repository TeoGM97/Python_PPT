#Rock Paper Scissors Game

user_option = input('Rock, Papaer o Scissors? => ')
pc_option = 'Rock'

#Tie Validation
if user_option == pc_option:
    print('Tie')

#Game Logic (Win and Lose)
#User uses Rock vs Scissors and Paper
elif user_option == 'Rock':
    if pc_option == 'Scissors':
        print('Rock gana a Scissors')
        print('YOU WIN')
    else:
        print('Paper gana a Rock')
        print('GAME OVER')

#User uses Paper vs Rock and Scissors
elif user_option == 'Paper':
    if pc_option == 'Rock':
        print('Paper gana a Scissors')
        print('YOU WIN')
    else:
        print('Scissors gana a Paper')
        print('GAME OVER')

#User uses Scissors vs Paper and Rock
elif user_option == 'Scissors':
    if pc_option == 'Rock':
        print('Scissors gana a Paper')
        print('YOU WIN')
    else:
        print('Rock gana a Scissors')
        print('GAME OVER')