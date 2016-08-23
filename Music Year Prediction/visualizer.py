import numpy as np
import matplotlib.pyplot as plt

with open('training.bin', 'r') as f:
    trn = np.load(f)
    years = np.unique(trn[:,0])

    mean = np.array([])
    for year in years:
        try:
            rng = (trn[:,0]==year).nonzero()[0]

            avg = np.zeros(90)
            for i in rng:
                avg = np.add(avg, trn[i][1:])
            avg = avg/len(rng)
            avg = np.append([year], avg)
            if not len(mean):
                mean = np.array([avg])
            else:
                mean = np.append(mean, np.array([avg]), axis=0)

            print "[SUCCESS] Calculated mean vectors of ", year
        except:
            print "[FAILED] COuld not calculate mean for ", year

    with open('mean.bin', 'wb') as fi:
        np.save(fi, mean)
        print "[SUCCESS] Saved as `mean.bin` "
