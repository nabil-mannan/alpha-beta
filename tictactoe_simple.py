import random
import time

HUMAN = 1
COMPUTER = -1
FREE = 0

board = [[FREE, FREE, FREE],
         [FREE, FREE, FREE],
         [FREE, FREE, FREE]]


def game_board(b):
    board_piece = {HUMAN: 'X',
                   COMPUTER: 'O',
                   FREE: ' '}
    for name in b:
        for symbol in name:
            character = board_piece[symbol]
            print(' {} '.format(character), end='')  # End statement to prevent new lines
        print('\n' + '---------')


def winner(b, player):
    # The different combinations that result in a win i.e., rows, columns, and diagonals
    winComb = [[b[0][0], b[0][1], b[0][2]],
               [b[1][0], b[1][1], b[1][2]],
               [b[2][0], b[2][1], b[2][2]],
               [b[0][0], b[1][0], b[2][0]],
               [b[0][1], b[1][1], b[2][1]],
               [b[0][2], b[1][2], b[2][2]],
               [b[0][0], b[1][1], b[2][2]],
               [b[0][2], b[1][1], b[2][0]]]
    if [player, player, player] in winComb:
        return True
    else:
        return False


def who_won(b):  # Prints the result of game
    if winner(b, HUMAN):
        print('You have won!')
    elif winner(b, COMPUTER):
        print('Unlucky, you lose!')
    else:
        print("It's a draw")


def free_spaces(b):
    free = []
    for x, row in enumerate(b):
        for y, col in enumerate(row):
            if b[x][y] == FREE:
                free.append([x, y])
    return free


def full_board(b):
    if len(free_spaces(b)) == 0:
        return True
    else:
        return False


board_pos = {1: [0, 0], 2: [0, 1], 3: [0, 2],
             4: [1, 0], 5: [1, 1], 6: [1, 2],
             7: [2, 0], 8: [2, 1], 9: [2, 2]}


def player_move(b):
    while True:
        try:
            move = int(input('Choose a move from (1-9) '))
            if move < 1 or move > 9:
                print('Position out of scope, please try again ')
            elif not (board_pos[move] in free_spaces(b)):
                print('Sorry, that position has been taken')
            else:
                b[board_pos[move][0]][board_pos[move][1]] = HUMAN
                game_board(b)
                break
        except(KeyError, ValueError):
            print('Please pick a number!')
        finally:
            print("Next move")


def computer_move(b):
    start = time.time()
    while True:
        result = random.randint(1, 9)
        if board_pos[result] in free_spaces(b):
            b[board_pos[result][0]][board_pos[result][1]] = COMPUTER
            game_board(b)
            break
        else:
            print('Sorry, that position has been taken')
    end = time.time()
    print('Evaluation time: {}s'.format(round(end - start, 10)))


def end_game(b):  # If a player has a matching combination, game ends
    return winner(b, HUMAN) or winner(b, COMPUTER)


def game(b):
    while True:
        try:  # Player can decide to go 1st or 2nd
            turn = input('Would you like to start? (Y/N)? ')
            if not (turn == 'Y' or turn == 'N'):
                print('Try again')
            else:
                break
        except ValueError:
            print('Please, enter a letter')

    if turn == 'Y':
        current_player = HUMAN
    else:
        current_player = COMPUTER

    # As long as board is not full or game over, game will continue running
    while not (end_game(board) or full_board(board)):
        if current_player == HUMAN:
            player_move(b)
        else:
            computer_move(b)
        current_player *= -1

    who_won(board)


def tic_tac_toe():
    print('Hello, welcome to Tic-Tac-Toe against an AI! \n')
    print('1  2  3 \n'
          '------- \n'
          '4  5  6 \n'
          '------- \n'
          '7  8  9 \n')
    game(board)


tic_tac_toe()
