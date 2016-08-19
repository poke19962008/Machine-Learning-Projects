import board
import numpy as np
import matplotlib.pyplot as plt
import pickle
import argparse

alpha = 0.0001
epochs = 35000
nHidden = 50

policy = []

'''
 Maps the state action pairs on the basis of constant policy function
'''
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


'''
 Calculates the  Average Mean Square Error of Neural Network
'''
def avgLoss(predOtp, otp):
    loss = np.square(predOtp - otp)
    loss = np.sum(loss, axis=1)/9
    return 0.5*np.sum(loss, axis=0)/len(otp)

def modulate(x):
    y = []
    for i in xrange(9):
        if x[i] == 1:
            y.append(1), y.append(1)
        elif x[i] == -1:
            y.append(-1), y.append(-1)
        else:
            y.append(-1), y.append(1)
    return y

'''
 Build the model of Neural Network
'''
def build(P):
    source, target = P[:,0], P[:,1]
    weight = np.zeros((9*2, 9*2))

    for i in xrange(len(P)):
        sourceModulated = modulate(source[i])
        targetModulated = modulate(target[i])

        weight += np.transpose([sourceModulated])*targetModulated
    return weight


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--mapPolicy", action="store_true", default=False, dest="mapPolicy", help="Mpas the the state action value pair")

    parser.add_argument("--trainNN", action="store_true", default=False, dest="trainNN", help="Train the Neural Network")

    res = parser.parse_args()

    if res.mapPolicy:
        f = open("trained.bin", "rb")
        V = np.load(f)
        calcPolicy(V)
        f = open("policy.bin", "wb")
        np.save(f, np.array(policy))

    if res.trainNN:
        f = open("policy.bin", "rb")
        P = np.load(f)
        weight = build(P)

        print "weight: \n", weight
        with open('ann.pickle', 'wb') as handle:
            pickle.dump(weight, handle)

        plt.show()
