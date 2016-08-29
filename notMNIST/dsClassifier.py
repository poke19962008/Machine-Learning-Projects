import numpy as np
from scipy import misc
import pickle
import os

def loadLetter(rootFolder):
    folders = os.listdir(rootFolder)
    pixelDepth = 255.0

    for label in folders:
        images = os.listdir(os.path.join(rootFolder, label))

        for image in images:
            imageFile = os.path.join(rootFolder, folder, image)
            image = (misc.imread(imageFile)-pixelDepth/2)/pixelDepth


            break
        break


if __name__ == '__main__':
    rootFolder = 'data'

    loadLetter(rootFolder)
