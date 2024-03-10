"""
Tic Tac Toe Player
"""

import math
import copy
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
    num_X = sum(row.count(X) for row in board)
    num_O = sum(row.count(O) for row in board)
    return X if num_X == num_O else O
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise ValueError("Invalid action")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if all(cell == X for cell in row):
            return X
        elif all(cell == O for cell in row):
            return O
    
    # Check columns
    for j in range(3):
        if all(board[i][j] == X for i in range(3)):
            return X
        elif all(board[i][j] == O for i in range(3)):
            return O
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(all(cell != EMPTY for cell in row) for row in board)
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0
    #raise NotImplementedError


# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """
#     def max_value(board):
#         if terminal(board):
#             return utility(board)
#         v = float('-inf')
#         for action in actions(board):
#             v = max(v, min_value(result(board, action)))
#         return v
    
#     def min_value(board):
#         if terminal(board):
#             return utility(board)
#         v = float('inf')
#         for action in actions(board):
#             v = min(v, max_value(result(board, action)))
#         return v
    
#     if terminal(board):
#         return None
    
#     best_action = None
#     best_value = float('-inf')
#     for action in actions(board):
#         value = min_value(result(board, action))
#         if value > best_value:
#             best_value = value
#             best_action = action
#     return best_action
#     #raise NotImplementedError
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        if terminal(board):
            return utility(board)
        v = float('-inf')
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v
    
    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float('inf')
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v
    
    if terminal(board):
        return None
    
    player_turn = player(board)
    best_action = None
    if player_turn == X:
        best_value = float('-inf')
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
    else:
        best_value = float('inf')
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
    
    return best_action
