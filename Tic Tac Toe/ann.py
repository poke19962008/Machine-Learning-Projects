import board
import numpy as np

alpha = 0.1
epochs = 1
nHidden = 20

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

def build(P):
    W1 = np.zeros((9, nHidden))
    W2 = np.zeros((nHidden, 9))
    B1 = np.zeros((1, nHidden))
    B2 = np.zeros((1, 9))

    ann = {}

    for i in xrange(epochs):
        for inp, otp in P:
            Z1 = inp.dot(W1) + B1
            a1 = np.tanh(Z1)
            Z2 = a1.dot(W2)  + B2
            predOtp = np.tanh(Z2)

            


    return ann


if __name__ == '__main__':
    # f = open("trained.bin", "rb")
    # V = np.load(f)
    # calcPolicy(V)
    #
    # f = open("policy.bin", "wb")
    # np.save(f, np.array(policy))

    f = open("policy.bin", "rb")
    build(np.load(f))
