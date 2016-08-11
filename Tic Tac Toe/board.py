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
        board.append(np.array([np.array([S_x, S_o]), 0.5, 0]))
    return np.array(board)


def hasEnd(state):
    state = np.reshape(state, (3, 3))
    for i in xrange(0, 3):
        v = np.sum(state, axis=0)
        h = np.sum(state, axis=1)

        if (3 in v) or (3 in h):
            return (True, 'x')
        elif (-3 in v) or (-3 in h):
            return (True, 'o')
    d1 = state[0][0] + state[1][1] + state[2][2]
    d2 = state[0][2] + state[1][1] + state[2][0]

    if (d1 == 3) or (d2 == 3):
        return (True, 'x')
    elif (d1 == -3) or (d2 == -3):
        return (True, 'o')

    zeroes = np.where(state == 0)
    if (not len(zeroes[0])) and (not len(zeroes[1])):
        return (True, 'xo')
    else:
        return (False, np.nan)


def nextStates(initState, player):
    states = np.empty((0, 9), int)
    for i in xrange(0, 9):
        if initState[i] == 0:
            x = np.array(initState)
            o = np.array(initState)
            x[i], o[i] = 1, -1
            if player == 'x':
                states = np.append(states, [x], axis=0)
            else:
                states = np.append(states, [o], axis=0)
    return np.array(states)

def getBoardIndex(state):
    S_o = S_x = 0
    for i in xrange(0, 9):

        if state[i] == 1.0:
            S_x += np.power(0.5, i)
        elif state[i] == -1.0:
            S_o += np.power(0.5, i)
    return np.array([S_x, S_o])
