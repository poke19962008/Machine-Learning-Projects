import numpy as np
'''
    X: 1
    O: -1
    b: 0
'''
def combinations():
    board = []
    for i in xrange(0, 19683):
        c = i
        S_x = S_o = 0
        for j in xrange(0, 9):
            if c%3 == 1:
                S_x += np.power(0.5, j)
            elif c%3 == 2:
                S_o += np.power(0.5, j)
            c /= 3
        board.append(np.array([S_x, S_o, 0.5]))
    return np.array(board)

# def hasWin(state):


def nextStates(initState, player):
    states = []
    for i in xrange(0, 9):
        if initState[i] == 0:
            x = np.array(initState)
            o = np.array(initState)
            x[i], o[i] = 1, -1
            states.append(x) if player == 'x' else states.append(o)
    return np.array(states)
