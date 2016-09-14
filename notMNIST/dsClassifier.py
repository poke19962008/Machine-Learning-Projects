import numpy as np
from scipy import misc
import pickle
import os
import matplotlib.pyplot as plt

def loadLetter(rootFolder):
    folders = os.listdir(rootFolder)
    pixelDepth = 255.0

    for label in folders:
        images = os.listdir(os.path.join(rootFolder, label))
        npImages = []
        for image in images:
            imageFile = os.path.join(rootFolder, label, image)
            try:
                image = (misc.imread(imageFile)-pixelDepth/2)/pixelDepth
                npImages.append(image)

                print "[SUCCESS] Loaded: ", imageFile
                print "Mean: ", np.mean(image)
                print "Standard Deviation: ", np.std(image), "\n\n"
            except:
                print "[FAIL] Cannot Load: ", imageFile, "\n\n"
            break
        break
        with open('bin/letters/%s.pkl'%label, 'wb') as f:
            pickle.dump(np.array(npImages), f)

def mergeDatasets():
    trainingSet, validSet, testSet = [], [], []
    trainingLabel, validLabel, testLabel = [], [], []

    pickles = os.listdir("bin/letters")

    for pkl in pickles:
        with open("bin/letters/%s"%pkl, 'rb') as f:
            letterSet = pickle.load(f)

            trainSize = int(letterSet.shape[0]*0.8)
            testSize = int(letterSet.shape[0]*0.2)
            validSize = int(trainSize*0.2)

            label = [pkl.split(".")[0]]
            trainingLabel = np.append(trainingLabel, label*trainSize)
            testLabel = np.append(testLabel, label*testSize)
            validLabel = np.append(validLabel, label*validSize)

            if not len(trainingSet):
                trainingSet = letterSet[:trainSize,:,:]
                testSet = letterSet[trainSize:trainSize+testSize,:,:]
                validSet = letterSet[:validSize,:,:]
                continue

            trainingSet =np.append(trainingSet, letterSet[:trainSize,:,:], axis=0)
            testSet = np.append(testSet, letterSet[trainSize:trainSize+testSize,:,:], axis=0)
            validSet = np.append(validSet, letterSet[:validSize,:,:], axis=0)

    print "Training Set: ", trainingSet.shape, trainingLabel.shape
    print "Validation Set: ", validSet.shape, validLabel.shape
    print "Testing Set: ", testSet.shape, testLabel.shape

    return trainingSet, trainingLabel, validSet, validLabel, testSet, testLabel


if __name__ == '__main__':
    rootFolder = 'data'

    # loadLetter(rootFolder)
    mergeDatasets()
