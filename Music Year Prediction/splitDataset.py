import numpy as np

with open('YearPredictionMSD.txt', 'r') as rawDataSet:
    rawDataSet = rawDataSet.read().split("\n")
    trainingSet, testSet = [], []

    for i in xrange(len(rawDataSet)):
        tmp = rawDataSet[i].split(",")
        if i<=463715:
            trainingSet.append(tmp)
        else:
            testSet.append(tmp)
    print "[SUCCESS] Parsed Files"

    with open('training.bin', 'wb') as f:
        np.save(f, trainingSet)
        print "[SUCCESS] Saved training set."
    with open('test.bin', 'wb') as f:
        np.save(f, testSet)
        print "[SUCCESS] Saved test set."
        
    print "Training Set: training.bin"
    print "Test Set: test.bin"
