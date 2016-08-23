import numpy as np
import matplotlib.pyplot as plt

features = {
    'loudness': 1,
    'brightness': 2,
    'flatness': 3,
    'attack': 4,
    'b1': 5,
    'b2': 6,
    'b3': 7,
    'b4': 8,
    'b5': 9,
    'b6': 10,
    'b7': 11,
    'b8': 12,
}

def meanGrapher(ftr):
    with open('bin/mean.bin', 'r') as f:
        mean = np.load(f)
        plt.plot(mean[:,0], mean[:,features[ftr]], 'o', label="mean"+ftr)
        plt.xlabel('Year')
        plt.ylabel('Mean of average '+ftr)
        plt.title('Mean '+ftr)

def allFourMeanPlotter():
    meanGrapher('loudness')
    meanGrapher('brightness')
    meanGrapher('flatness')
    meanGrapher('attack')

def allBPlotter():
    ftrs = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8']

    for ftr in ftrs:
        plt.subplot(4, 2, ftrs.index(ftr)+1)
        meanGrapher(ftr)


if __name__ == '__main__':
    # allFourMeanPlotter()
    allBPlotter()

    plt.legend()
    plt.show()
