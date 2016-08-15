import board
import numpy as np
import signal, sys
import random as rnd

initState = [0]*9
boards = []

'''
 Constants Used
 discountFact: Discount Factor for Temporal Difference Learning Algorithm
 stepFactor: Step Size
 Epsilon: Greedy Factor
 rewards: reward points for the win, loss and draw match
'''
discountFact = 0.9
stepFactor = 0.09
epsilon = 0.1
rewards = {
    'win': 1,
    'loss': 0,
    'draw': 0.5
}

'''
 Search the state from the look up table
'''
def getStateInfo(state):
    for i in xrange(len(boards)):
        if len(np.where(np.all(boards[i][0] == state))[0]):
            return boards[i][1], len(boards[i][2]), i
            break

'''
 Policy Selection
'''
def pi(states):
    V_Si = []
    for state in states:
        V, freq, ind = getStateInfo(state)
        V_Si.append(V)

    iPi = np.argmax(V_Si)
    return states[iPi]

'''
 Recursive qLearning Method
'''

def rlLearn(state, turn):
    global boards, discountFact, stepFactor, epsilon, rewards

    V, freq, ind = getStateInfo(state)
    player = 'x' if turn else 'o'

    stepFactor_ = stepFactor/freq if freq else stepFactor

    nextStates = board.nextStates(state, player)

    rand = rnd.random()
    if rand < epsilon:  # Greedy Move
        nextMove = pi(nextStates)
    else:  # Random Move
        iNextMove = rnd.randint(0, len(nextStates)-1)
        nextMove = nextStates[iNextMove]


    hasEnd = board.hasEnd(nextMove)
    if hasEnd[0]:
        print hasEnd[1], " Won"
        if hasEnd[1] == 'x':
            return rewards['win']
        elif hasEnd[0] == 'o':
            return rewards['loss']
        else:
            return rewards['draw']

    nextStateV = rlLearn(nextMove, not turn)
    boards[ind][1] += stepFactor_*(nextStateV - boards[ind][1])
    boards[ind][2].append(boards[ind][1])

    print state, player, boards[ind][1]
    return boards[ind][1]

'''
 Save Board Before Termination
'''
def saveBoards(signal, frame):
    print "\n\nSaving Trained Datasets"
    f = file("trained.bin","wb")
    np.save(f, boards)

    print "[SUCCESS] BoardSaved"
    exit()

if __name__ == '__main__':

    signal.signal(signal.SIGINT, saveBoards)

    print "Loading Board Configs"
    boards = board.combinations(rewards)
    print "Loaded ", len(boards), " Boards\n"

    while True:
        rlLearn(initState, 1)
        print "--------END--------"
