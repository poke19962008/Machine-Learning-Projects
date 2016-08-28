import numpy as np
from sklearn import svm
from sklearn.externals import joblib

timbreVector = {
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

def learn(fName, features, nRows=-1):
    with open('bin/train.bin', 'r') as f:
        train = np.load(f)

        minYear = 1922

        x = np.mat(train[:nRows,timbreVector[features[0]]]).reshape(nRows,1)
        y = np.mat(train[:nRows,timbreVector[features[1]]]).reshape(nRows,1)
        z = np.mat(train[:nRows,timbreVector[features[2]]]).reshape(nRows,1)

        X = np.concatenate((x, y, z), axis=1)
        Y = train[:nRows,0] % minYear

        clf = svm.SVC()
        clf.fit(X, Y)
        print "[SUCCESS] Fitted training data to SVM (kernel: rbf)."

        print "[STARTED] Dumping classifier."
        joblib.dump(clf, 'bin/%s'%fName)
        print "[SUCCESS] Dumped to ", fName



if __name__ == '__main__':
    features = ['loudness', 'b2', 'b3']
    fName = "svmf167.pkl"

    learn(fName, features)
