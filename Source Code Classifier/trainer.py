from features import extract
from reStore import markerList
from sklearn.naive_bayes import GaussianNB
import numpy as np
import os, pickle

langs = ['py', 'java', 'rb', 'cpp', 'c']
tRatio = 0.7 # Training/Validation ratio

def train():
    with open('./bin/train.bin', 'rb') as f:
        ds = pickle.load(f)
        XTrain, yTrain = ds['X'], ds['y']
        del ds

    with open('./bin/validation.bin', 'rb') as f:
        ds = pickle.load(f)
        XValidation, yValidation = ds['X'], ds['y']
        del ds

    clf = GaussianNB()
    clf.fit(XTrain, yTrain)

    print "Training Set Length:", XTrain.shape
    print "Test Set Length:", XValidation.shape
    print "Test Scores:", clf.score(XValidation, yValidation)

    with open('./bin/gnbClf.bin', 'wb') as f:
        pickle.dump(clf, f)
        print "[SUCCESS] Saved classifier as `gnbClf.bin`"

def getTrainDS():
    root = './data'
    X = np.mat([0]*(len(markerList)))
    y = np.array([])

    for lang in langs:
        for scDir in os.listdir(os.path.join(root, lang)):
            sc = getSC(os.path.join(root, lang, scDir))

            feature = extract(sc)
            feature = np.asmatrix(feature)

            X = np.append(X, feature, axis=0)
            X = np.asmatrix(X)
            y = np.append(y, [lang])

            print "[SUCCESS] Extracted", scDir

            del feature
    X = X[1:]

    print "Shuffling datasets."
    X, y = shuffle(X, y)
    print "[SUCCES] Shuffled datasets"

    print "Splitting and saving datasets."
    ds = splitDS(X, y)
    print "[SUCCESS] Splitted datasets."
    saveDS(ds)
    print "[SUCCESS] Saved datasets."

    del X, y


def saveDS(ds):
    with open('./bin/train.bin', 'wb') as f:
        pickle.dump(ds['training'], f)

    with open('./bin/validation.bin', 'wb') as f:
        pickle.dump(ds['validation'], f)


def splitDS(X, y):
    tLen = int(len(X)*tRatio)
    return {
        'training': {
            'X': X[:tLen, ::],
            'y': y[:tLen]
        },
        'validation': {
            'X': X[tLen:, ::],
            'y': y[tLen:]
        }
    }

def shuffle(X, y):
    permut = np.random.permutation(X.shape[0])

    X, y = X[permut,::], y[permut]
    return X, y


def getSC(dir):
    with open(dir) as f:
        return f.read()

if __name__ == '__main__':
    # getTrainDS()
    train()
