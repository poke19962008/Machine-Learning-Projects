# -*- coding: utf-8 -*-
import os, re
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
from cleaner import clean


def tokenize(text):
    return re.findall(r'[\w\']+|[\"\"!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~\"\"\\]', text)

def extractDoc(ext):
    root = 'data'
    data = []
    for f in os.listdir(os.path.join(root, ext))[:5]:
        with open(os.path.join(root, ext, f), 'r') as sc:
            sc = clean(sc.read(), 'cpp')
            data.append(sc)
            print "[SUCCESS] Read", os.path.join(root, ext, f)


    vectorizer = TfidfVectorizer(tokenizer=tokenize, ngram_range=(1,2))
    X = vectorizer.fit_transform(data)
    del data

    features_by_gram = defaultdict(list)
    for f, w in zip(vectorizer.get_feature_names(), vectorizer.idf_):
        features_by_gram[len(f.split(' '))].append((f, w))
    top_n = 50

    for gram, features in features_by_gram.iteritems():
        top_features = sorted(features, key=lambda x: x[1], reverse=True)[:top_n]
        top_features = [f[0] for f in top_features]
        print '{}-gram top:'.format(gram), top_features


if __name__ == '__main__':
    extractDoc('cpp')
