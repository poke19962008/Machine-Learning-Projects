from __future__ import division
import matplotlib.pyplot as plt
from reStore import  markerList
from scipy.stats import norm, gaussian_kde
import numpy as np
import pickle, re

np.set_printoptions(threshold=np.inf)

langs = ['py', 'java', 'rb', 'cpp', 'c']
fig = plt.figure()

def getValue(lang='py', type='freq'):
    X, y = getDS()

    ind = np.where(y == lang)[0]
    X = X[ind, ::]

    if type == 'raw':
        return X

    freq = np.array([], dtype='float16')
    freq = np.sum(X, axis=0)

    if type == 'freq':
        return np.squeeze(np.asarray(freq))


    prob = freq/np.sum(freq)
    prob = np.squeeze(np.asarray(prob))

    print "Probability argmax:", prob[np.argmax(prob)]
    print "Argmax Pattern:", markerList[np.argmax(prob)].pattern

    return prob



def featureMapHist(lang='py', normed=True):
    freq = getValue(lang, type='freq')
    raw = np.array([])

    for i in xrange(len(freq)):
        raw = np.append(raw, [i]*freq[i])
    print "[SUCCESS] Calculated raw for", lang

    (mu, sigma) = np.mean(raw), np.std(raw)
    pdf = norm.pdf(raw, mu, sigma)

    if not normed:
        plt.plot(raw, pdf, label="%s"%lang)
    else:
        ax = fig.add_subplot(3, 2, langs.index(lang)+1)
        plt.plot(raw, pdf)
        ax.hist(raw, normed=True, alpha=0.75)
        ax.set_title(lang)

def featureMapDensity(lang='py', normed=True):
    freq = getValue(lang, type='freq')
    raw = np.array([])

    for i in xrange(len(freq)):
        raw = np.append(raw, [i]*freq[i])
    print "[SUCCESS] Calculated raw for", lang

    gaussKDE = gaussian_kde(raw, bw_method=0.5)
    ind = np.linspace(1, 115, 200)

    plt.plot(ind, gaussKDE(ind), label="%s"%lang)

def getDS():
    with open('./bin/train.bin', 'rb') as f:
        ds = pickle.load(f)
        return ds['X'], ds['y']

if __name__ == '__main__':
    [featureMapHist(x, normed=True) for x in langs]

    plt.xlabel('Markers')
    plt.ylabel('Probability')

    plt.legend()
    plt.show()
