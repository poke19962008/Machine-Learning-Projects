import matplotlib.pyplot as plt
import numpy as np

f = open('trained.bin', 'rb')
V = np.load(f)

samples = [[0,  0,  0,  1, 0, 0, 0,  0,  0],
           [-1,  0,  0,  1, 1, 0, 0,  -1,  0]]

for sample in samples:
    for v in V:
        if len(np.where(np.all(v[0] == sample, axis=0))[0]):
            plt.plot(range(len(v[2])), v[2], label=str(sample))
            break
plt.legend()
plt.show()
