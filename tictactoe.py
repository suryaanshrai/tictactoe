"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount = 0
    ocount = 0
    for i in board:
        for j in i:
            if j == X:
                xcount += 1
            elif j == O:
                ocount += 1
    if xcount == ocount:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleMoves = set()
    row = 0
    for i in board:
        col = 0
        for j in i:
            if j == EMPTY:
                possibleMoves.add((row, col))
            col += 1
        row += 1
    return possibleMoves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player1 = player(board)
    if board[action[0]][action[1]] != None:
        raise Exception
    else:
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player1
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checking each column
    for i in range(3):
        xcount = 0
        ocount = 0
        for j in range(3):
            if board[i][j] == X:
                xcount += 1
            elif board[i][j] == O:
                ocount += 1
        if xcount == 3:
            return 'x'
        elif ocount == 3:
            return 'o'

    # Checking each row
    for j in range(3):
        xcount = 0
        ocount = 0
        for i in range(3):
            if board[i][j] == X:
                xcount += 1
            elif board[i][j] == O:
                ocount += 1
        if xcount == 3:
            return 'x'
        elif ocount == 3:
            return 'o'

    # Checking diagonals
    xcount = 0
    ocount = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                if board[i][j] == X:
                    xcount += 1
                elif board[i][j] == O:
                    ocount += 1
    if xcount == 3:
        return 'x'
    elif ocount == 3:
        return 'o'

    xcount = 0
    ocount = 0
    for i in range(3):
        for j in range(3):
            if i+j == 2:
                if board[i][j] == X:
                    xcount += 1
                elif board[i][j] == O:
                    ocount += 1
    if xcount == 3:
        return 'x'
    elif ocount == 3:
        return 'o'

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    emptycount = 0
    for i in board:
        for j in i:
            if j == EMPTY:
                emptycount += 1
    if emptycount == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    curr_winner = winner(board)
    if curr_winner == 'x':
        return 1
    elif curr_winner == 'o':
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        possible_moves = []
        for action in actions(board):
            possible_moves += [(action, min_value(result(board, action)))]
        possible_moves.sort(key=lambda x: x[1], reverse=True)
        return possible_moves[0][0]
    else:
        possible_moves = []
        for action in actions(board):
            possible_moves += [(action, max_value(result(board, action)))]
        possible_moves.sort(key=lambda x: x[1])
        return possible_moves[0][0]


def max_value(board):
    v = -100000
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    v = 100000
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v