import board
import numpy as np

policy = []

def calcPolicy(V):
    global policy

    for i in xrange(len(V)):
        if np.sum(V[i][0]) or board.hasEnd(V[i][0])[0]:
            continue

        afterStates = board.nextStates(V[i][0], 'x')
        vAfterStates = []
        for j in xrange(len(afterStates)):
            for k in xrange(len(V)):
                find = np.where(np.all(afterStates[j] == V[k][0], axis=0))
                if len(find[0]):
                    vAfterStates.append([V[k][0], V[k][1]])
                    break
        if len(afterStates):
            vAfterStates = np.array(vAfterStates)
            piInd = np.argmax(vAfterStates[:,1])
            print V[i][0], vAfterStates[piInd][0]
            policy.append([V[i][0], vAfterStates[piInd][0]])

if __name__ == '__main__':
    f = open("trained.bin", "rb")
    V = np.load(f)
    calcPolicy(V)

    f = open("policy.bin", "wb")
    np.save(f, np.array(policy))
