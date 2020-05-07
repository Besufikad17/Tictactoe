def check(b):
    if (b[0][0] == b[1][1] == b[2][2]) or (b[0][2] == b[1][1] == b[0][2]) or (b[0][1] == b[1][1] == b[2][1]) or (b[1][0] == b[1][1] == b[1][2]):
        return True
    else:
        return False


def get_no_moves(b):
    count = 0
    for i in range(0,len(b)):
        for j in range(0,len(b[0])):
            if b[i][j] == '':
                pass
            else:
                count = count + 1
    return count


def is_board_full(b):
    count = 0
    for i in b:
        for j in i:
            if j.startswith('_'):
                pass
            else:
                count = count + 1
    if count == 9:
        return True
    else:
        return False


def play(turn,board):
    no_moves = get_no_moves(board)
    if no_moves >= 5:
        c = check(board)
        c2 = is_board_full(board)
        if turn == 0:
            if c is True:
                return ('player 1 won')
            else:
                if c2 is True:
                    return ('Draw!')
                else:
                    pass
        else:
            if c is True:
                return ('player 2 won')
            else:
                if c2 is True:
                    return ('Draw!')
                else:
                    pass
    else:
        return None



