from Computer import play_computer

game_mode = input('Game Mode : ')


def get_value(game_mode):
    if game_mode.startswith('2 player'):
        val1 = input('Value 1 : ')
        val2 = input('Value 2 : ')
        valuess = [val1, val2]
        return valuess
    elif game_mode.startswith('single player'):
        val1 = input('Value 1 : ')
        return val1
    else:
        return 'Invalid Game Mode'    


values = get_value(game_mode)


def get_position(str):
    pos = []
    i = int(str[0])
    j = int(str[2])
    pos = [i,j]
    return pos


def play(vals,game_mode):
    if vals == 'Invalid Game Mode':
        print('Invalid Game Mode')
    else:
        if game_mode.startswith('2 player'):
            board = [['_','_','_'],['_','_','_'],['_','_','_']]
            i = 0
            while i >= 0:
                if i % 2 == 0:
                    command = input('player 1 : ')
                    if command[4].startswith(vals[0]):
                        positions = get_position(command)
                        board[positions[0]][positions[1]] = command[4]
                        print(board)
                        if i >= 4:
                            c = check(board)
                            c2 = is_board_full(board)
                            if c is True:
                                print('player 1 won')
                                break
                            else:
                                if c2 is True:
                                    print('Draw!')
                                else:
                                    pass
                        else:
                            pass
                    else:
                        print('Invalid Value')
                        break
                else:
                    command = input('player 2 : ')
                    if command[4].startswith(vals[1]):
                        positions = get_position(command)
                        board[positions[0]][positions[1]] = command[4]
                        print(board)
                        if i >= 4:
                            c = check(board)
                            c2 = is_board_full(board)
                            if c is True:
                                print('player 1 won')
                                break
                            else:
                                if c2 is True:
                                    print('Draw!')
                                else:
                                    pass
                        else:
                            pass
                    else:
                        print('Invalid Value')
                        break
                i = i + 1
        else:
            board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
            i = 0
            while i >= 0:
                if i % 2 == 0:
                    command = input('player  : ')
                    if command[4].startswith(vals[0]):
                        positions = get_position(command)
                        board[positions[0]][positions[1]] = command[4]
                        print(board)
                        if i >= 4:
                            c = check(board)
                            c2 = is_board_full(board)
                            if c is True:
                                print('player  won')
                                break
                            else:
                                if c2 is True:
                                    print('Draw!')
                                else:
                                    pass
                        else:
                            pass
                    else:
                        print('Invalid Value')
                        break
                else:
                    value = ''
                    if vals.startswith('X'):
                        value = 'O'
                    else:
                        value = 'X'
                    command = play_computer(board,value)
                    print('Computer : ' + command)
                    pos = get_position(command)
                    board[pos[0]][pos[1]] = command[4]
                    print(board)
                i = i + 1


def check(b):
    if (b[0][0] == b[1][1] == b[2][2]) or (b[0][2] == b[1][1] == b[0][2]) or (b[0][1] == b[1][1] == b[2][1]) or (b[1][0] == b[1][1] == b[1][2]):
        return True
    else:
        return False



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

        

play(values,game_mode)
          

