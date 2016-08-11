import signal, sys
import numpy as np
import board

discountFact = 0.85
stepFactor = 0.25
rewards = {
    'win': 1,
    'loss': -1,
    'draw': -1
}
generation = {
    'success': 0,
    'failed': 0,
    'total': 0
}
evolutions = 0
temperture = 200

boards = None


def tdLearn(path, hasWin):
    global discountFact, stepFactor, rewards, generation, evolutions, boards

    if hasWin[1] == 'x':
        reward = rewards['win']
        Vprev = reward
    else:
        reward = rewards['loss']
        Vprev = reward

    if not generation['total'] % 10:
        if generation['success'] < 2:
            stepFactor *= stepFactor
        else:
            stepFactor /= stepFactor
        generation['success'] = 0
        generation['failed'] = 0

    bIndex = board.getBoardIndex(path[-1])
    for i in xrange(0, len(boards)):
        if len(np.where(np.all(boards[i][0] == bIndex, axis=0))[0]):
            boards[i][1] = 1
            boards[i][2] = rewards['win']
            print path[-1], boards[i][1]

    for j in xrange(len(path)-2, 0, -1):
        bIndex = board.getBoardIndex(path[j])
        for i in xrange(0, len(boards)):
            if len(np.where(np.all(boards[i][0] == bIndex, axis=0))[0]):
                V = boards[i][2]
                boards[i][2] += stepFactor*(discountFact*Vprev + V)

                boards[i][1] = getPolicy(boards[i][2], path[j])
                boards[i][3].append(boards[i][1])

                print path[j], boards[i][1]
                break

    generation['total'] += 1

def getPolicy(V, state):
    global temperture
    return np.exp(V/temperture) / getSumVsi(state)

def getSumVsi(states):
    afterStates = []
    global temperture

    x = board.nextStates(states, 'x')
    o = board.nextStates(states, 'o')

    if len(x) and len(o):
        states = np.concatenate((x, o), axis=0)
    elif len(x):
        states = x
    elif len(o):
        states = o

    for i  in xrange(0, len(states)):
        bIndex = board.getBoardIndex(states[i])

        for j in xrange(len(boards)):
            if len(np.where(np.all(boards[j][0] == bIndex, axis=0))[0]):
                afterStates.append(np.exp(boards[j][2]/temperture))
    return np.sum(afterStates)

def train():
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

        hasWin = board.hasEnd(curState)
        if not hasWin[0]:
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
            tdLearn(path, hasWin)
            print "----------------END----------------"

def saveBoards(signal, frame):
    print "\n\nSaving Trained Datasets"
    f = file("trained.bin","wb")
    np.save(f, boards)
    print "[SUCCESS] Saved"

    sys.exit(0)

if __name__ == '__main__':

    signal.signal(signal.SIGINT, saveBoards)

    print  "Loading boards..."
    boards = board.combinations()
    print  "Loaded ", len(boards)

    print "\n\nStarted Training"
    print  "Press ctrl+c to close and save the trained dataset"
    train()
