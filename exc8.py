def rock_paper_scissors():
    print('Valid choices: rock, paper, scissors.\n')
    p1 = input('Player 1 choice: ')
    p2 = input('Player 2 choice: ')

    if p1 == 'rock':
        if p2 == 'rock':
            print('Draw. None of the Players won.')
        elif p2 == 'paper':
            print('Player 2 wins!')
        elif p2 == 'scissors':
            print('Player 1 wins!')
    elif p1 == 'paper':
        if p2 == 'rock':
            print('Player 1 wins!')
        elif p2 == 'paper':
            print('Draw. None of the Players won.')
        elif p2 == 'scissors':
            print('Player 2 wins!')
    elif p1 == 'scissors':
        if p2 == 'rock':
            print('Player 2 wins!')
        elif p2 == 'paper':
            print('Player 1 wins!')
        elif p2 == 'scissors':
            print('Draw. None of the Players won.')
    else:
        print('Invalid input.')

def main():
    cont = True
    while cont:
        rock_paper_scissors()
        dec = input('Would you like to play again? (yes/no)')

        if dec == 'no':
            cont = False

main()

