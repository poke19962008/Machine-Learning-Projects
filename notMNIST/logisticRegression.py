# Logistic Regression model
# Accuracy: 86.577540107
# Training Time: 102.33870101 sec
# Prediction Time: 0.0539240837097 sec
# Number of records: 14974

import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.image as mpimg
import os, pickle, time

def model():
    with open("bin/notMNIST.pkl", 'r') as f:
        alphabTest = pickle.load(f)

        X = alphabTest["trainingSet"]
        X = X[:len(X)].reshape(len(X), 28*28) # Image Dimension is 28*28
        Y = alphabTest["trainingLabel"]
        del alphabTest

        logreg = LogisticRegression()
        start_time = time.time()
        classifier = logreg.fit(X, Y)
        print("Training Time: %s sec" % (time.time() - start_time))

        del X, Y
        with open('bin/lrClssr.pkl', 'wb') as f:
            pickle.dump(classifier, f)
            print "[SUCCESS] Saved as lrClssr.pkl"


def predict():
    with open('bin/lrClssr.pkl', 'r') as f:
        classifier = pickle.load(f)

        with open("bin/notMNIST.pkl", 'r') as f:
            alphabTest = pickle.load(f)

            X = alphabTest["testSet"]
            X = X[:len(X)].reshape(len(X), 28*28) # Image Dimension is 28*28
            Y = alphabTest["testLabel"]
            del alphabTest

            start_time = time.time()
            classifier.predict(X)
            print("Prediction Time: %s sec" % (time.time() - start_time))
            pred = classifier.score(X, Y)

            print "Accuracy: ", pred

if __name__ == '__main__':
    model()
    predict()
