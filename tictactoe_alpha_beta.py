import math
import random
import time

HUMAN = 1
COMPUTER = -1
FREE = 0  # Free is a placeholder for the board pieces

board = [[FREE, FREE, FREE],
         [FREE, FREE, FREE],
         [FREE, FREE, FREE]]  # 3x3 array in the shape of the board


def game_board(b):
    board_piece = {HUMAN: 'X',
                   COMPUTER: 'O',
                   FREE: ' '}  # A dictionary that assigns the players to the board pieces
    for name in b:             # Then iterating over all positions on the board
        for symbol in name:    # Where symbol represents the values the players are equal to above
            character = board_piece[symbol]
            print(' {} '.format(character), end='')  # End statement needed to prevent new lines
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
    if [player, player, player] in winComb:  # You are a winner if your board pieces match any combination
        return True
    else:
        return False


def who_won(b):
    if winner(b, HUMAN):
        print('You have won!')
    elif winner(b, COMPUTER):
        print('Unlucky, you lose!')
    else:
        print("It's a draw")


def free_spaces(b):
    free = []
    for x, row in enumerate(b):  # Adds a counter, essentially creating a tuple
        for y, col in enumerate(row):
            if b[x][y] == FREE:  # Iterating over all board positions and appends to list if the position is equal to FREE
                free.append([x, y])
    return free


def full_board(b):
    if len(free_spaces(b)) == 0:
        return True
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
            elif not (board_pos[move] in free_spaces(b)):  # If the coordinate is not in free spaces meaning it has been taken
                print('Sorry, that position has been taken')
            else:
                b[board_pos[move][0]][board_pos[move][1]] = HUMAN  # Board updates with new row and column indices
                game_board(b)
                break
        except(KeyError, ValueError):
            print('Please pick a number!')
        finally:
            print("Next move")


def get_score(b):
    if winner(b, HUMAN):
        return 1
    elif winner(b, COMPUTER):
        return -1
    else:
        return 0


def end_game(b):  # If a player has a matching combination, game ends
    return winner(b, HUMAN) or winner(b, COMPUTER)


def alpha_beta(b, depth, alpha, beta, maximiser):
    row = -1
    col = -1
    if depth == 0 or end_game(b):  # If the depth of search is at the first layer, i.e., the game is already over
        return [row, col, get_score(b)]

    # Uncomment for algorithm to choose random position for its first move
    elif len(free_spaces(b)) == 9:
        row = random.randint(0,2)
        col = random.randint(0,2)
        return [row, col, get_score(b)]
    
    else:
        for space in free_spaces(b): # Checks alpha-beta value for every free position on the board, returns list of coordinates
            b[space[0]][space[1]] = maximiser
            eva = alpha_beta(b, depth - 1, alpha, beta, -maximiser)
            if maximiser == HUMAN:
                if eva[2] > alpha:
                    alpha = eva[2]
                    row = space[0]
                    col = space[1]
            else:
                if eva[2] < beta:
                    beta = eva[2]
                    row = space[0]
                    col = space[1]
            b[space[0]][space[1]] = FREE

            if alpha >= beta:
                break

        if maximiser == HUMAN:
            return [row, col, alpha]
        else:
            return [row, col, beta]


alpha = -math.inf
beta = math.inf


def computer_move(b):
    start = time.time()
    result = alpha_beta(b, len(free_spaces(b)), alpha, beta, COMPUTER)
    b[result[0]][result[1]] = COMPUTER
    game_board(b)
    end = time.time()
    print('Evaluation time: {}s'.format(round(end - start, 10)))


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
    print('Hello, welcome to Tic-Tac-Toe against an unbeatable AI! \n')
    print('1  2  3 \n'
          '------- \n'
          '4  5  6 \n'
          '------- \n'
          '7  8  9 \n')
    game(board)


tic_tac_toe()
