import sklearn
from sklearn.datasets import make_moons
from array import array
import matplotlib.pyplot as plt
import numpy as np

X = Y = []
alpha = 0.015
numRecords = 0

def plt_decision_boundary(pred_func):
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01

    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape((xx.shape))

    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Spectral)


def predict(x, net):
    W1, B1, W2, B2 = net['W1'], net['B1'], net['W2'], net['B2']

    z1 = x.dot(W1) + B1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + B2
    expScores = np.exp(z2)
    probs = expScores / np.sum(expScores, axis=1, keepdims=True)

    return np.argmax(probs, axis=1)


def loss(net):
    W1, B1, W2, B2 = net['W1'], net['B1'], net['W2'], net['B2']

    z1 = X.dot(W1) + B1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + B2
    expScores = np.exp(z2)
    probs = expScores / np.sum(expScores, axis=1, keepdims=True)

    predictClass = np.argmax(probs, axis=1)
    loss = 0.5*np.power(predictClass - Y, 2)

    return np.sum(loss)/numRecords


def build(hlayer, epochs=350):
    W1 = np.random.randn(2, hlayer)
    B1 = np.zeros((1, hlayer))
    W2 = np.random.randn(hlayer, 2)
    B2 = np.zeros((1, 2))

    net = {}
    lossFn = []

    for i in xrange(0, epochs):
        z1 = X.dot(W1) + B1
        a1 = np.tanh(z1)
        z2 = a1.dot(W2) + B2
        expScores = np.exp(z2)
        probs = expScores / np.sum(expScores, axis=1, keepdims=True)

        delta2 = probs
        delta2[range(numRecords), Y] -= 1

        delta1 = delta2.dot(W2.T) * (1 - np.power(a1, 2))

        dW2 = (a1.T).dot(delta2)
        dB2 = np.sum(delta2, axis=0, keepdims=True)
        dW1 = (X.T).dot(delta1)
        dB1 = np.sum(delta1, axis=0, keepdims=True)

        W1 += -alpha*(dW1)
        B1 += -alpha*(dB1)
        W2 += -alpha*(dW2)
        B2 += -alpha*(dB2)

        net = {
            "W1": W1,
            "B1": B1,
            "W2": W2,
            "B2": B2
        }

        error = loss(net)*100
        lossFn.append([i, error])
        if i%25 == 0:
            print i, "th Iteration, Loss: ", error, "%"
    return net, np.array(lossFn)


if __name__ == "__main__":
    X, Y = make_moons(200, noise=0.2)
    numRecords = len(X)

    net, lossFn = build(3)

    plt.subplot(211)
    plt.title("Boundary Classification")
    plt_decision_boundary(lambda x: predict(x, net))

    plt.subplot(212)
    plt.ylabel("Error")
    plt.xlabel("Epochs")
    plt.title("Error Functions")
    plt.plot(lossFn[:, 0], lossFn[:, 1])
    plt.show()
