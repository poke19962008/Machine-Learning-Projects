import numpy as np
import board

alpha = 0.9
discountFact = 0.85
reward = {
    'win': 1,
    'loss': -1,
    'draw': -1
}
generation = 0
evolutions = 0

def train(boards):
    initState = np.zeros(9)
    player = 'x'
    xStack = np.array([initState])
    oStack = np.array([initState])

    parent = np.empty((1, 9))
    parent[:] = np.nan
    child = [[initState]]

    path = np.array([initState])
    paths = []
    hasEnd = False

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

        if hasEnd:
            hasEnd = False
            spliceInd = -1
            for i in xrange(0, len(paths)):
                spliceInd = np.where(np.all(parent[pInd] == paths[i], axis=1))
                if len(spliceInd[0]):
                    spliceInd = spliceInd[0][0]
                    break
            path = np.delete(path, np.s_[spliceInd+1::], 0)

        path = np.append(path, [curState], axis=0)
        if not board.hasEnd(curState)[0]:
            nextMove = board.nextStates(curState, 'o' if player == 'x' else 'x')
            parent = np.append(parent, [curState], axis=0)
            child.append(nextMove)
            if player == "x":
                xStack = np.append(xStack, nextMove, axis=0)
            else:
                oStack = np.append(oStack, nextMove, axis=0)
        else:
            hasEnd = True
            paths.append(path)
            print path
            print "----------------END----------------"

if __name__ == '__main__':
    boards = board.combinations()
    train(board)
