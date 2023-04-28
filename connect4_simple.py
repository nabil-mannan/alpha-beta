import numpy as np
import random

no_of_rows = 6
no_of_columns = 7

HUMAN = 1
COMPUTER = 2


def create_board():
    board = np.zeros((6, 7), dtype=int)
    return board


def has_space(board, col):
    # Checks if the row is empty to allow a piece to move and ensures column is not full
    for col in range(no_of_columns):
        if board[5][col] == 0:
            return True


def next_free_row(board, col):
    # Returns the index of row where there is an empty space, where a piece can be placed
    for row in range(no_of_rows):
        if board[row][col] == 0:
            return row


def print_board(board):
    # Flips the board
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


# while not game_over:
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
                print('\n', 'Computer calculating next move...')
                break
        except(KeyError, ValueError):
            print('Please pick a number!')


def computer_move(board):
    while True:
        result = random.randint(0, 6)
        # Computer will drop a piece on the board
        if has_space(board, result):
            row = next_free_row(board, result)
            board[row][result] = COMPUTER
            print('  0 1 2 3 4 5 6')
            print_board(board)
            break
        else:
            print("Column is full, try again")


def who_won(board):  # Prints the result of the game
    if winner(board, HUMAN):
        print('You win!')
    elif winner(board, COMPUTER):
        print('Unlucky, you lose!')
    else:
        print("It's a draw")


def finished(board):  # If a player has a matching combination, game ends
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
    while not finished(board):
        if current_player == HUMAN:
            player_move(board)
        else:
            computer_move(board)
        current_player += 1
        current_player = current_player % 2

    print_board(board)
    who_won(board)


def connect4():
    print('Hello, welcome to Connect-4 against an AI! \n')
    board = create_board()
    print('  0 1 2 3 4 5 6')
    print_board(board)
    print()
    game(board)


connect4()
