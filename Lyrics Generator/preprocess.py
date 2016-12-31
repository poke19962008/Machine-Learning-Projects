import os, re
from nltk.tokenize import word_tokenize
import numpy as np

def clean(d):
    d = re.sub(r'\[[0-9]x\]', "", d)
    d = re.sub(r'\[Chorus\]', "", d)
    return d

if __name__ == '__main__':
    print clean("Reaper [4x]")
    root = "./dump"
    tokens = np.array([])

    # Extract and clean files
    for fdir in os.listdir(root):
        with open(os.path.join(root, fdir), 'r') as f:
            l = clean(f.read())
            ftoken = word_tokenize(l)
            tokens = np.append(tokens, ftoken)
            print "Parsed ", fdir
        print "Token vector size: ", tokens.size


    # One Hot Encoder
