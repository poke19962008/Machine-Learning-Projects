import os, re, pickle
from nltk.tokenize import word_tokenize
import numpy as np
from sklearn.preprocessing import LabelEncoder

def clean(d):
    d = re.sub(r'\[[0-9]x\]', "", d)
    d = re.sub(r'\[Chorus\]', "", d)
    return d

if __name__ == '__main__':
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


    # Token Encoder
    le = LabelEncoder()
    le.fit(tokens)
    with open('encoder.bin', 'wb') as f:
        pickle.dump(le, f)
        print "Pickled Encoed as `encoder.bin`"
