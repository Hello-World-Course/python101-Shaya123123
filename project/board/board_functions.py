def is_on_board(x, y, board):
    # This is wrong fix it:
    if 0 <= x < len(board[0]) and 0 <= y < len(board):
        return True
    else:
        return False

def safe_set_value(x, y, value, board):
    if is_on_board(x, y, board):
        board[x][y] = value
        return True
    else:
        return False

