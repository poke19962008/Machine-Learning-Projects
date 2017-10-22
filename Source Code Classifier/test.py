import pickle
from features import extract

'''
Test Files:
- ./data/test/GCAC.txt
- ./data/test/trainer.txt
'''

testFile = "./data/test/GCAC.txt"
clf = pickle.load(file('./bin/gnbClf.bin', 'r'))
with open(testFile) as f:
    sc = f.read()
    feat = extract(sc)
    print "Testing: ", testFile
    print "Predicted: ", clf.predict([feat])[0]
