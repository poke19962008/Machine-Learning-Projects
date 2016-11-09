from __future__ import division
import matplotlib.pyplot as plt
from reStore import  markerList
import numpy as np
import pickle, re

langs = ['py', 'java', 'rb', 'cpp', 'c']
fig = plt.figure()

def featureMap(lang='py'):
    X, y = getDS()

    ind = np.where(y == lang)[0]
    X = X[ind, ::]

    prob = np.array([], dtype='float16')
    prob = np.sum(X, axis=0)
    prob = prob/np.sum(prob)
    prob = np.squeeze(np.asarray(prob))

    print "Probability argmax:", prob[np.argmax(prob)]
    print "Argmax Pattern:", markerList[np.argmax(prob)].pattern

    ax = fig.add_subplot(3, 2, langs.index(lang)+1)
    ax.bar(np.arange(prob.shape[0]), prob)
    ax.set_title(lang)


def getDS():
    with open('./bin/train.bin', 'rb') as f:
        ds = pickle.load(f)
        return ds['X'], ds['y']

if __name__ == '__main__':
    [featureMap(x) for x in langs]
    plt.show()
