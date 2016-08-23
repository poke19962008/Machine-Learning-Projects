from __future__ import division
import numpy as np


def calculateMean(trn):
    with open('training.bin', 'r') as f:
        trn = np.load(f)
        years = np.unique(trn[:,0])

        mean = np.array([])
        for year in years:
            try:
                rng = (trn[:,0]==year).nonzero()[0]

                avg = np.zeros(90)
                for i in rng:
                    avg = np.add(avg, trn[i][1:])
                avg = avg/len(rng)
                avg = np.append([year], avg)
                if not len(mean):
                    mean = np.array([avg])
                else:
                    mean = np.append(mean, np.array([avg]), axis=0)

                print "[SUCCESS] Calculated mean vectors for year ", year
            except:
                print "[FAILED] COuld not calculate mean for year ", year

        with open('mean.bin', 'wb') as fi:
            np.save(fi, mean)
            print "[SUCCESS] Saved as `mean.bin` "

def saveFile(trainingSet, testSet):
    with open('training.bin', 'wb') as f:
        np.save(f, trainingSet)
        print "[SUCCESS] Saved training set."
    with open('test.bin', 'wb') as f:
        np.save(f, testSet)
        print "[SUCCESS] Saved test set."

    print "Training Set: training.bin"
    print "Test Set: test.bin"



if __name__ == '__main__':
    with open('YearPredictionMSD.txt', 'r') as rawDataSet:
        rawDataSet = rawDataSet.read().split("\n")
        print "[SUCCESS] Loaded raw dataset"
        trainingSet, testSet = [], []

        for i in xrange(len(rawDataSet)):
            tmp = rawDataSet[i].split(",")
            try:
                tmp = [float(x) for x in tmp]
                tmp[0] = int(tmp[0])
            except:
                print "Could not convert ", tmp, " to float"
            if i<=463715:
                trainingSet.append(tmp)
            else:
                testSet.append(tmp)
        print "[SUCCESS] Parsed Files"

        saveFile(trainingSet, testSet)
        calculateMean(trainingSet)
