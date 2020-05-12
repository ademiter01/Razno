
    #Rock beats scissors
    #Scissors beats paper
    #Paper beats rock

player1 = input('This is Rock, Pappers, Scissors. Enter first letter (R, P or S) to make your play\nPlayer 1: ')
player2 = input('Your turn, Player 2. Choose R, P or S.\nPlayer 2: ')

if len(player1) > 1 or len(player2) > 1:
    print('Invalid input. Please use only letters R, P and S')
if len(player1) < 1 or len(player2) < 1:
    print('Invalid input. Please use only letters R, P and S')


valid_inp = ['R','P','S','r','p','s']


if player1.upper() not in valid_inp or player2.upper() not in valid_inp:
    print('Invalid input. Please use only letters R, P and S')


if player1.upper() == player2.upper():
    print("")
    print("It's a draw!")

print("")
if player1.upper() == 'P' and player2.upper() == 'S':
    print('Congratulations, Player 2! \nScissors beat paper.')
elif player1.upper() == 'S' and player2.upper() == 'P':
    print('Congratulations, Player 1! \nScissors beat paper.')

if player1.upper() == 'R' and player2.upper() == 'S':
    print('Congratulations, Player 1! \nRock beats scissors.')
elif player2.upper() == 'R' and player1.upper() =='S':
    print('Congratulations, Player 2! \nRock beats scissors.')

if player1.upper() == 'P' and player2.upper() == 'R':
    print('Congratulations, Player 1! \nPaper beats rock.')
elif player2.upper() == 'P' and player1.upper() == 'R':
    print('Congratulations, Player 1! \nPaper beats rock.')
print("")
print('Thanks for playing!')
