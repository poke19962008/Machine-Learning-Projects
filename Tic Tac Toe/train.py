from __future__ import division
import signal, sys
import numpy as np
import board

'''
 Constants Used
 discountFact: Discount Factor for Temporal Difference Learning Algorithm
 stepFactor: Step Size
 rewards: reward points for the win, loss and draw match
 temperture: Temperature Policy Selection using Boltzman Distribution
'''
discountFact = 0.9
stepFactor = 0.09
rewards = {
    'win': 1,
    'loss': 0,
    'draw': 0.5
}

epochs = 0
boards = None

'''
 Temporal Difference Learning
'''
def tdLearn(path, hasWin):
    global discountFact, stepFactor, rewards, generation, boards, epochs
    stepFactor_ = stepFactor

    if hasWin[1] == 'x':
        reward = rewards['win']
    elif hasWin[1] == 'o':
        reward = rewards['loss']
    else:
        reward = rewards['draw']
    Vprev = reward

    for j in xrange(len(path)-2, 0, -1):
        for i in xrange(0, len(boards)):
            if len(np.where(np.all(boards[i][0] == path[j], axis=0))[0]):
                stepFactor = len(boards[i][2])
                if stepFactor == 0:
                    stepFactor = 1
                else:
                    stepFactor = 1/stepFactor

                # Update V(S)
                V = boards[i][1]
                boards[i][1] += stepFactor*(discountFact*Vprev - V)

                boards[i][2].append(boards[i][1])

                print path[j], boards[i][1], stepFactor, hasWin[1]
                break

    epochs += 1


'''
 Starts the Learning of each possible path
'''
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
            if not len(xStack):
                break
            curState = xStack[len(xStack)-1]
            xStack = np.delete(xStack, len(xStack)-1, axis=0)
        else:
            if not len(oStack):
                break
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
    saveBoards(None, None)

'''
 Save Board Before Termination
'''
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
    print  "Loaded ", len(boards), "Boards"

    print "\n\nStarted Training"
    print  "Press ctrl+c to close and save the trained dataset"
    train()
