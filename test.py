from tictactoe import actions, min_value, result
board = [
    [None, None, 'X'],
    ['X', None, None],
    ['X', 'O', 'O']
]
possible_moves = []
for action in actions(board):
    possible_moves += [(action, min_value(result(board, action)))]
possible_moves.sort(key=lambda x:x[1], reverse=True)
print(possible_moves)
print(actions(board))
for i in possible_moves:
    print(i[1])