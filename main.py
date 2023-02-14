#Rock Paper Scissors Game
import random

#Rounds counter
rounds = 1

#Options function
def choose_options():
    #Tuple of options
    options = ('rock', 'paper', 'scissors')

    #Input user option
    user_option = input('Rock, Papaer o Scissors? => ')
    #Standarize input
    user_option = user_option.lower()

    #No valid option message
    if not user_option in options:
        print('  ')
        print('=> Are you okay? ')
        #continue
        #Si elije una opcion no valida, retorne none
        return None, None

    #Random selection of pc in options tuple
    pc_option = random.choice(options)

    #Show options in screen
    print('  ')
    print('User Option =>', user_option)
    print('PC Option =>', pc_option)
    print('  ')

    return user_option, pc_option

#Function with game rules
def check_rules(user_option, pc_option, user_wins, pc_wins):
    #Tie Validation
    if user_option == pc_option:
        print('Tie')

    #User uses Rock vs Scissors or Paper
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

    #User uses Paper vs Rock or Scissors
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

    #User uses Scissors vs Paper or Rock
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

#Main Function to run the game
def run_game():
    #Victories
    pc_wins = 0
    user_wins = 0

    #Loop to validate who wins 2 times
    while True:

        print('--' * 10)
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        print('  ')

        #Display of wins
        print('USER WINS', user_wins)
        print('PC WINS', pc_wins)

        rounds += 1

        #Function with user and pc option
        user_option, pc_option = choose_options()

        #Function with game rules
        check_rules(user_option, pc_option)

        #Defeat message
        if pc_wins == 2:
            print('💀DEFEAT💀')
            break

        # Victory message
        if user_wins == 2:
            print('🍻VICTORY🍻')
            break

