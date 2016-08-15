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


'''
 Build the model of Neural Network
'''
def build(P):
    error = []

    # with open('ann.pickle', 'rb') as handler:
    #     model = pickle.load(handler)
    #     W1, W2, B1, B2 = model["W1"], model["W2"], model["B1"], model["B2"]

    W1 = np.random.randn(9, nHidden)
    W2 = np.random.randn(nHidden, 9)
    B1 = np.zeros((1, nHidden))
    B2 = np.zeros((1, 9))

    ann = {}

    for i in xrange(epochs):
        Z1 = P[:,0].dot(W1) + B1
        a1 = np.tanh(Z1)
        Z2 = a1.dot(W2)  + B2
        predOtp = np.tanh(Z2)
        predOtp = np.around(predOtp)

        delta2 = predOtp
        delta2 = predOtp - P[:,1]
        delta1 = delta2.dot(W2.T) * (1 - np.power(a1, 2))

        dW2 = (a1.T).dot(delta2)
        dB2 = np.sum(delta2, axis=0, keepdims=True)
        dW1 = (P[:,0].T).dot(delta1)
        dB1 = np.sum(delta1, axis=0, keepdims=True)

        W1 += -alpha*(dW1)
        B1 += -alpha*(dB1)
        W2 += -alpha*(dW2)
        B2 += -alpha*(dB2)

        ann = {
            "W1": W1,
            "B1": B1,
            "W2": W2,
            "B2": B2
        }
        loss = avgLoss(predOtp, P[:,1])
        if not i%100:
            print "Epoch=", i, "Loss(MSE)=", loss
        error.append([i, loss])
    error = np.array(error)
    plt.plot(error[:,0], error[:,1])
    return ann

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
        model = build(P)
        with open('ann.pickle', 'wb') as handle:
            pickle.dump(model, handle)

        plt.show()
