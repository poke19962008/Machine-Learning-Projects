import numpy as np
from sklearn import svm
from sklearn.externals import joblib
import matplotlib.pyplot as plt

'''
 Results:
    classifier: svmf167t70000.pkl
    train: 70,000
    test: 30,000
    <MSE>: 73.35
    <Abs. Diff.>: 7.14
'''
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

        clf = svm.SVC(verbose=3)
        clf.fit(X, Y)
        print "[SUCCESS] Fitted training data to SVM (kernel: rbf)."

        print "[STARTED] Dumping classifier."
        joblib.dump(clf, 'bin/%s'%fName)
        print "[SUCCESS] Dumped to ", fName

def predict(fName, X):
    clf = joblib.load(fName)
    return clf.predict(X) + minYear

def test(fName, features, nRows):
    with open('bin/train.bin') as f:
        test = np.load(f)

        x = np.mat(test[:nRows,timbreVector[features[0]]]).reshape(nRows,1)
        y = np.mat(test[:nRows,timbreVector[features[1]]]).reshape(nRows,1)
        z = np.mat(test[:nRows,timbreVector[features[2]]]).reshape(nRows,1)

        X = np.concatenate((x, y, z), axis=1)
        Y = test[:nRows,0]
        pred = predict(fName, X)

        print "Mean Square Error: ", np.mean(0.5*np.square(pred - Y))
        print "Absolute Error: ", np.mean(np.absolute(pred-Y))

        plt.scatter(Y, pred-Y, marker='o')
        plt.xlabel('Actual')
        plt.ylabel('Difference')
        plt.show()


if __name__ == '__main__':
    features = ['loudness', 'b2', 'b3']
    fName = "svmf167t70000.pkl"

    # learn(fName, features, 70000)
    test('bin/'+fName, features, 30000)
