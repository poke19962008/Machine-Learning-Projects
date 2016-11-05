from sklearn import tree
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

import numpy as np
import pandas as pd
import pickle, pydotplus

'''
Encodings:
    Gender
        Male: 0
        Femal: 1

Selected Features:
    Pclass
    Age
    Sex
'''

def clean(type="train"):
    if type=='train':
        df = pd.read_csv('train.csv')
    else:
        df = pd.read_csv('test.csv')


    # Normalise Columns
    df.Age = (df.Age - df.Age.mean())/(df.Age.max() - df.Age.min())
    df.Fare = (df.Fare - df.Fare.mean())/(df.Fare.max() - df.Fare.min())


    # Remove all NaN values
    dfg = df[np.isnan(df.Age)]

    df = df[np.isfinite(df.Age)]
    df = df[np.isfinite(df.Pclass)]
    df = df[np.isfinite(df.Fare)]

    df['Sex'] = df['Sex'].replace(['male', 'female'], [0, 1])
    dfg['Sex'] = dfg['Sex'].replace(['male', 'female'], [0, 1])
    dfg['Embarked'] = dfg['Embarked'].replace(['C', 'Q', 'S'], [1, 2, 3])

    X = pd.DataFrame({'Pclass': df['Pclass'], 'Age': df['Age'], 'Sex': df['Sex'], 'Fare': df['Fare'], 'SibSp': df['SibSp']})

    Xg = pd.DataFrame({'Pclass': dfg['Pclass'], 'Sex': dfg['Sex'], 'Embarked': dfg['Embarked'], 'SibSp': dfg['SibSp']})

    X = X.as_matrix()
    Xg = Xg.as_matrix()

    if type=='train':
        Y = df['Survived'].as_matrix()
        Yg = dfg['Survived'].as_matrix()

        return {
            'validation': {
                'X': X[int(0.7*len(X)):],
                'Xg': Xg[int(0.7*len(Xg)):],
                'Y': Y[int(0.7*len(Y)):],
                'Yg': Yg[int(0.7*len(Yg)):]
            },
            'train': {
                'X': X,
                'Xg': Xg,
                'Y': Y,
                'Yg': Yg,
            }
        }
    else:
        pid = df['PassengerId']
        pidg = dfg['PassengerId']
        return X, Xg, pid, pidg
# Models
def models(X,Xg,Xv,Xgv, Y,Yg,Yv, Ygv):
    clfs = {
        'rf': [RandomForestClassifier(bootstrap=True,
            criterion='entropy', max_depth=None, max_features=2,
            max_leaf_nodes=16, min_samples_split=10, n_estimators=1000,
            n_jobs=-1, oob_score=False), RandomForestClassifier(bootstrap=True,
            criterion='entropy', max_depth=None, max_features=2,
            max_leaf_nodes=16, min_samples_split=10, n_estimators=1000,
            n_jobs=-1, oob_score=False)],
        'lr': [LogisticRegression(), LogisticRegression()],
        'svm': [svm.SVC(kernel='rbf', gamma=3), svm.SVC(kernel='rbf', gamma=3)]
    }

    best = -1
    clfSelected = []
    for clfName in clfs:
        clf = clfs[clfName]

        clf[0].fit(X, Y)
        clf[1].fit(Xg, Yg)

        scoreP = clf[0].score(Xv, Yv)*100
        scoreS = clf[1].score(Xgv, Ygv)*100

        print "[SUCCESS] Fitted %s classifier\n"%clfName

        print "Cross-Validating model from `train.csv`"
        print "Primary Classifier Result"
        print "Length of validation set: ", len(Xv)
        print "Accuracy: ", scoreP , "%"

        print "\nSecondary Classifier Result"
        print "Length of validation set: ", len(Xgv)
        print "Accuracy: ", scoreS, "%\n"

        if np.mean([scoreP, scoreS]) > best:
            best = np.mean([scoreP, scoreS])
            clfSelected = [clf[0], clf[1], clfName]

    print "-"*20
    print "Selected: ", clfSelected[2]
    print "Score: ", best
    return clfSelected



def fit():
    dataset = clean()
    Xv, Xgv, Yv, Ygv = dataset['validation']['X'], dataset['validation']['Xg'], dataset['validation']['Y'], dataset['validation']['Yg']
    X, Xg, Y, Yg = dataset['train']['X'],dataset['train']['Xg'],  dataset['train']['Y'], dataset['train']['Yg']

    del dataset

    clf, clfg, _ = models(X,Xg,Xv,Xgv, Y,Yg,Yv, Ygv)

    with open('clfp.bin', 'wb') as f:
        pickle.dump(clf, f)

        print "[SUCCESS] Saved primary classifier to `clfp.bin`"

    with open('clfs.bin', 'wb') as f:
        pickle.dump(clfg, f)
        print "[SUCCESS] Saved secondary classifier to `clfs.bin`"
    del clf, clfg, Xg, Yg, X, Y, Xv, Yv


def predict():
    X, Xg, pid, pidg = clean('test')

    with open('clfp.bin', 'rb') as f:
        clf = pickle.load(f)
        print "[SUCCESS] Loaded primary classifier"

    with open('clfs.bin', 'rb') as f:
        clfg = pickle.load(f)
        print "[SUCCESS] Loaded primary classifier"

    H = clf.predict(X)
    print "[SUCCESS] End of primary prediction"

    Hg = clfg.predict(Xg)
    print "[SUCCESS] End of secondary prediction"

    pid = pid.append(pd.Series([1044]))
    H = np.append(H, [1])

    df = pd.DataFrame({'PassengerId': pid, 'Survived': H})
    dfg = pd.DataFrame({'PassengerId': pidg, 'Survived': Hg})
    df = pd.concat([df, dfg])

    df.set_index('PassengerId', inplace=True)
    df.to_csv('submit.csv')
    print "[SUCCESS] Saved as `submit.csv`"

if __name__ == '__main__':
    fit()
    # predict()
