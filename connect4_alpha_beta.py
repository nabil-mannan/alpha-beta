import numpy as np
import math
import time

no_of_rows = 6
no_of_columns = 7

HUMAN = 1
COMPUTER = 2


def create_board():
    board = np.zeros((6, 7), dtype=int)
    return board


def has_space(board, col):
    # if this condition is true we will let the use drop piece here.
    # if not true that means the col is not vacant
    return board[5][col] == 0


def next_free_row(board, col):
    for r in range(no_of_rows):
        if board[r][col] == 0:
            return r


def free_spaces(board):
    free = []
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            if board[x][y] == 0:
                free.append([x, y])
    return free


def full_board(board):
    if len(free_spaces(board)) == 0:
        return True
    return False


def print_board(board):
    print(np.flip(board, 0))


def winner(board, piece):
    # Check horizontal positions for win
    for c in range(no_of_columns - 3):
        for r in range(no_of_rows):
            if board[r][c] == board[r][c + 1] == board[r][c + 2] == board[r][c + 3] == piece:
                return True

    # Check vertical positions for win
    for c in range(no_of_columns):
        for r in range(no_of_rows - 3):
            if board[r][c] == board[r + 1][c] == board[r + 2][c] == board[r + 3][c] == piece:
                return True

    # Check upwards sloping diagonals
    for c in range(no_of_columns - 3):
        for r in range(no_of_rows - 3):
            if board[r][c] == board[r + 1][c + 1] == board[r + 2][c + 2] == board[r + 3][c + 3] == piece:
                return True

    # Check downward sloping diagonals
    for c in range(no_of_columns - 3):
        for r in range(3, no_of_rows):
            if board[r][c] == board[r - 1][c + 1] == board[r - 2][c + 2] == board[r - 3][c + 3] == piece:
                return True


def who_won(board):  # Prints the result of the game
    if winner(board, HUMAN):
        print('You win!')
    elif winner(board, COMPUTER):
        print('Unlucky, you lose!')
    else:
        print("It's a draw")


def get_score(board):
    if winner(board, HUMAN):
        return 1
    elif winner(board, COMPUTER):
        return -1
    else:
        return 0


def alpha_beta(b, depth, alpha, beta, maximiser):
    row = 0
    col = 0
    if depth == 0 or end_game(b):  # If the depth of search is at the first layer, i.e., the game is already over
        return [row, col, get_score(b)]

    else:
        for space in free_spaces(b): # Checks alpha-beta value for every free position on the board
            b[space[0]][space[1]] = maximiser
            eval = alpha_beta(b, depth - 1, alpha, beta, -maximiser)
            if maximiser == HUMAN:
                if eval[2] > alpha:
                    alpha = eval[2]
                    row = space[0]
                    col = space[1]
            else:
                if eval[2] < beta:
                    beta = eval[2]
                    row = space[0]
                    col = space[1]
            b[space[0]][space[1]] = 0

            if alpha >= beta:
                break

        if maximiser == HUMAN:
            return [row, col, alpha]
        else:
            return [row, col, beta]


alpha = -math.inf
beta = math.inf


def player_move(board):
    while True:
        try:
            col = int(input("Player, choose a move from (0-6): "))
            # Player 1 will drop a piece on the board
            if col < 0 or col > 6:
                print("Move is out of range, try again")
            elif not has_space(board, col):
                print("Column is full, try again")
            else:
                row = next_free_row(board, col)
                board[row][col] = HUMAN
                print_board(board)
                print('Computer calculating next move...')
                break
        except(KeyError, ValueError):
            print('Please pick a number!')


def computer_move(board):
    # Computer will drop a piece on the board
    start = time.time()
    result = alpha_beta(board, 4, alpha, beta, -1)
    row = next_free_row(board, result[1])
    board[row][result[1]] = COMPUTER
    print('  0 1 2 3 4 5 6')
    print_board(board)
    end = time.time()
    print('Evaluation time: {}s'.format(round(end - start, 5)))


def end_game(board):  # If a player has a matching combination, game ends
    return winner(board, COMPUTER) or winner(board, HUMAN)


def game(board):
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

    # As long as the game is not over, game will continue running
    while not (end_game(board) or full_board(board)):
        if current_player == HUMAN:
            player_move(board)
        else:
            computer_move(board)
        # current_player += 1
        current_player = (current_player + 1) % 2

    print_board(board)
    who_won(board)


def connect4():
    print('Hello, welcome to Connect-4 against an unbeatable AI! \n')
    board = create_board()
    print('  0 1 2 3 4 5 6')
    print_board(board)
    print()
    game(board)


connect4()
