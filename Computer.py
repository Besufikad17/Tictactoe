from random import randint


def get_free_positions(b):
    free_positions = []
    for i in range(0,len(b)):
        for j in range(0,len(b[0])):
            if b[i][j] == '_':
                free_positions.append(str(i) + ',' + str(j))
            else:
                pass
    return free_positions


def play_computer(b,val):
    moves = [['0,0','1,1','2,2'],['0,1','1,1','2,1'],['0,2','1,1','2,0'],['1,0','1,1','1,2']]
    possible_positions = get_free_positions(b)
    i = randint(0,len(possible_positions)-1)
    return possible_positions[i] + ' ' + val

