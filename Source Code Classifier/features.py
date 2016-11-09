import numpy as np
from reStore import markerList, tokenizer
import re

def extract(sc):
    freq = [0]*len(markerList)
    for i in xrange(len(markerList)):
        freq[i] = len(re.findall(markerList[i], sc))
    return np.array(freq, dtype='int16')

if __name__ == '__main__':
    with open('./data/cpp/accum.cpp') as f:
        print extract(f.read())
