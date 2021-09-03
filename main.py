from random import randint

box = {'7': ' ', '8': ' ', '9': ' ',
       '4': ' ', '5': ' ', '6': ' ',
       '1': ' ', '2': ' ', '3': ' '}


def print_board():
    print(f' {box["7"]} | {box["8"]} | {box["9"]}  \n'
          f'---+---+---\n'
          f' {box["4"]} | {box["5"]} | {box["6"]}  \n'
          f'---+---+---\n'
          f' {box["1"]} | {box["2"]} | {box["3"]}  ')


def clear_board():
    for key in box:
        box[key] = ' '


print('TIC-TAC-TOE')
start = True


def game():
    players = input('How many players? (1 or 2): ')
    player1 = 'X'
    player2 = 'O'
    print('** Please note the board is based on a computer NumPad. **')

    print_board()
    turn_count = 1

    while turn_count < 10:
        if players == '2':
            if turn_count % 2 != 0:
                move = input(f"Where do you want to move '{player1}'? ")
                if box[move] != ' ':
                    print('That space is occupied. Please choose somewhere else.')
                    continue
                else:
                    box[move] = player1
                    turn_count += 1
                    print_board()
            else:
                move = input(f"Where do you want to move '{player2}'? ")
                if box[move] != ' ':
                    print('That space is occupied. Please choose somewhere else.')
                    continue
                else:
                    box[move] = player2
                    turn_count += 1
                    print_board()
        else:
            if turn_count % 2 != 0:
                move = input(f"Where do you want to move '{player1}'? ")
                if box[move] != ' ':
                    print('That space is occupied. Please choose somewhere else.')
                    continue
                else:
                    box[move] = player1
                    turn_count += 1
                    print_board()
            else:
                move = str(randint(1, 9))
                if box[move] != ' ':
                    continue
                else:
                    box[move] = player2
                    turn_count += 1
                    print_board()

        # Look for winning combinations
        if turn_count > 5:
            # Horizontal wins
            if box['7'] == box['8'] == box['9']:
                print(f'{box["7"]} wins!')
                break
            elif box['4'] == box['5'] == box['6']:
                print(f'{box["4"]} wins!')
                break
            elif box['1'] == box['2'] == box['3']:
                print(f'{box["1"]} wins!')
                break
            # Vertical wins
            elif box['7'] == box['4'] == box['1']:
                print(f'{box["7"]} wins!')
                break
            elif box['8'] == box['5'] == box['2']:
                print(f'{box["8"]} wins!')
                break
            elif box['9'] == box['6'] == box['3']:
                print(f'{box["9"]} wins!')
                break
            # Diagonal wins
            elif box['7'] == box['5'] == box['3']:
                print(f'{box["7"]} wins!')
                break
            elif box['9'] == box['5'] == box['1']:
                print(f'{box["9"]} wins!')
                break
            elif turn_count == 10:
                print('Game ends in a Tie.')


while start:
    game()
    inquiry_loop = True
    while inquiry_loop:
        again = input("Do you want to play again? (y/n): ").lower()
        if again == 'y':
            clear_board()
            inquiry_loop = False
        elif again == 'n':
            start = False
            inquiry_loop = False
        else:
            print('Please enter a valid input.')


