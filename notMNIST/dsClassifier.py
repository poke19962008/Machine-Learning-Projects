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

                # plt.imshow(image)
                # plt.show()
            except:
                print "[FAIL] Cannot Load: ", imageFile, "\n\n"

        #     break
        # break
        with open('bin/letters/%s.pkl'%label, 'wb') as f:
            pickle.dump(np.array(npImages), f)

if __name__ == '__main__':
    rootFolder = 'data'

    loadLetter(rootFolder)
