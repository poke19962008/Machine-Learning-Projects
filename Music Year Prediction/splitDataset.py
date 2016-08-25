from __future__ import division
import numpy as np


def calculateMean(fname, rfile):
    rfile = open("%s"%rfile, 'r')
    data = np.load(rfile)

    years = np.unique(data[:,0])

    mean = np.array([])
    for year in years:
        try:
            rng = (data[:,0]==year).nonzero()[0]

            avg = np.zeros(90)
            for i in rng:
                avg = np.add(avg, data[i][1:])
            avg = avg/len(rng)
            avg = np.append([year], avg)
            if not len(mean):
                mean = np.array([avg])
            else:
                mean = np.append(mean, np.array([avg]), axis=0)

            print "[SUCCESS] Calculated mean vectors for year ", year
        except:
            print "[FAILED] COuld not calculate mean for year ", year

    with open('%s.bin'%fname, 'wb') as fi:
        np.save(fi, mean)
        print "[SUCCESS] Saved as `%s.bin` "%fname

def saveFile(trainingSet, testSet):
    with open('train.bin', 'wb') as f:
        np.save(f, trainingSet)
        print "[SUCCESS] Saved training set."
    with open('test.bin', 'wb') as f:
        np.save(f, testSet)
        print "[SUCCESS] Saved test set."

    print "Training Set: train.bin"
    print "Test Set: test.bin"



if __name__ == '__main__':
    with open('YearPredictionMSD.txt', 'r') as rawDataSet:
        rawDataSet = rawDataSet.read().split("\n")
        print "[SUCCESS] Loaded raw dataset"
        trainingSet = []
        testSet = []

        for i in xrange(len(rawDataSet)):
            tmp = rawDataSet[i].split(",")
            try:
                tmp = [float(x) for x in tmp]
                tmp[0] = int(tmp[0])

                if i<=463715:
                    trainingSet.append(tmp)
                else:
                    testSet.append(tmp)
            except:
                print "Could not convert ", tmp, " to float"

        print "[SUCCESS] Parsed Files"

        saveFile(trainingSet, testSet)
        calculateMean("trainMean", "train.bin")
        calculateMean("testMean", "test.bin")
