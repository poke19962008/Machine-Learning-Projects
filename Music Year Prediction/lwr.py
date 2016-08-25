import numpy as np
import matplotlib.pyplot as plt


bandwidth = 0.3
alpha=10

'''
 Gaussian based kernel
'''
def kernel(datapoint, Xi):
    sqDiff = np.square(datapoint-Xi)
    power = -(0.5*sqDiff)/(bandwidth**2)
    return alpha*np.exp(power)

'''
 Returns the weight matrix for the corresponding datapoint
'''
def getWeights(trainingDomain, datapoint):
    global bandwidth

    n = trainingDomain.shape[1]
    weights = np.mat(np.eye(n))
    for i in xrange(n):
        weights[i, i] = kernel(datapoint, trainingDomain.item(i))
    return weights

def predict(X, Y, datapoint):
    theta = learn(X, Y, datapoint)

    if theta == None:
        return False
    return np.around(theta*datapoint)[0,0]

'''
 Locally Weighted Regression using Batch Gradient Descent
'''
def learn(X, Y, datapoint):
    global alpha

    datapoint = np.mat(datapoint)
    Y = np.mat(Y)
    X = np.mat(X)

    weights = getWeights(X, datapoint)

    den = (X*weights)*X.T
    num = (X*weights)*Y.T

    try:
        return num*den.I
    except:
        return None

if __name__ == '__main__':
 with open('bin/train.bin', 'r') as ftrain:
     with open('bin/test.bin', 'r') as ftest:
        training, testing = np.load(ftrain), np.load(ftest)

        Ytrain, Xtrain = training[:,0], training[:,1]
        Ytest, Xtest = testing[:,0], testing[:,1]


        hyp = [predict(Xtrain, Ytrain, x) for x in Xtest]
        print "Errors: ", hyp-Ytest
        print "Average Absolute Error: ", 0.5*np.sum(np.absolute(hyp-Ytest))/Ytest.shape[0]
        print "Average Squared Error: ", 0.5*np.sum(np.square(hyp-Ytest))/Ytest.shape[0]

        plt.plot(Xtest,Ytest, 'o', color="r", label="Actual")
        plt.plot(Xtest, hyp, 'o', color="b", label="Predicted")
        plt.plot(Xtrain,Ytrain, 'o', color="y", label="Training")

        plt.xlabel('Year')
        plt.ylabel('Mean of average loudness')
        plt.title('LOSS Prediction | Loudness')

        axes = plt.gca()
        axes.set_ylim([1920,2020])

        plt.legend()
        plt.show()
