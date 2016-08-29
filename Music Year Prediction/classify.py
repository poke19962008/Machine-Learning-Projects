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
minYear = 1922

def learn(fName, features, nRows=-1):
    with open('bin/train.bin', 'r') as f:
        train = np.load(f)

        x = np.mat(train[:nRows,timbreVector[features[0]]]).reshape(nRows,1)
        y = np.mat(train[:nRows,timbreVector[features[1]]]).reshape(nRows,1)
        z = np.mat(train[:nRows,timbreVector[features[2]]]).reshape(nRows,1)

        X = np.concatenate((x, y, z), axis=1)
        Y = train[:nRows,0] % minYear

        clf = svm.SVC(verbose=2)
        clf.fit(X, Y)
        print "[SUCCESS] Fitted training data to SVM (kernel: rbf)."

        print "[STARTED] Dumping classifier."
        joblib.dump(clf, 'bin/%s'%fName)
        print "[SUCCESS] Dumped to ", fName

def predict(fName, features):
    clf = joblib.load(fName)

    return clf.predict(features) + minYear

def test(fName, features):
    with open('bin/train.bin') as f:
        test = np.load(f)[:100]

        x = np.mat(test[:nRows,timbreVector[features[0]]]).reshape(nRows,1)
        y = np.mat(test[:nRows,timbreVector[features[1]]]).reshape(nRows,1)
        z = np.mat(test[:nRows,timbreVector[features[2]]]).reshape(nRows,1)

        print predict()



if __name__ == '__main__':
    features = ['loudness', 'b2', 'b3']
    fName = "svmf167t2000.pkl"

    learn(fName, features, 20000)

    # test(fName)
