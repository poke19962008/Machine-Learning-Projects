import numpy as np
import board

def train(boards):
    initState = np.zeros(9)
    player = 'x'
    xStack = np.array([initState])
    oStack = np.array([initState])

    parent = np.empty((1, 9))
    parent[:] = np.nan
    child = [[initState]]

    while True:
        if player == "x":
            curState = xStack[len(xStack)-1]
            xStack = np.delete(xStack, len(xStack)-1, axis=0)
        else:
            curState = oStack[len(oStack)-1]
            oStack = np.delete(oStack, len(oStack)-1, axis=0)
        player = 'o' if player == 'x' else 'x'

        for i in xrange(0, len(child)):
            find = np.where(np.all(curState == child[i], axis=1))
            if len(find[0]):
                pInd = i
                break

        print parent[pInd], curState, player
        if not board.hasEnd(curState)[0]:
            nextMove = board.nextStates(curState, 'o' if player == 'x' else 'x')
            parent = np.append(parent, [curState], axis=0)
            child.append(nextMove)
            if player == "x":
                xStack = np.append(xStack, nextMove, axis=0)
            else:
                oStack = np.append(oStack, nextMove, axis=0)
        else:
            print "----------------END----------------"

if __name__ == '__main__':
    boards = board.combinations()
    train(board)
