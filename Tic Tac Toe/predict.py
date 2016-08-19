import board
import numpy as np
import pickle
import argparse

'''
 Predict on the basis of given Neural Network model
'''
def modulate(x):
    y = []
    for i in xrange(9):
        if x[i] == 1:
            y.append(1), y.append(1)
        elif x[i] == -1:
            y.append(-1), y.append(-1)
        else:
            y.append(-1), y.append(1)
    return y

def demodulate(x):
    y = []
    for i in xrange(0, 9*2, 2):
        if x[i] == 1 and x[i+1] == 1:
            y.append(1)
        elif x[i] == -1 and x[i+1] == -1:
            y.append(-1)
        else:
            y.append(0)
    return y

def predict(weight, inp):
    inp = modulate(inp)
    net = np.dot(weight, inp)

    predOtp = np.piecewise(net, [net<0, net>0], [-1, 1])
    return demodulate(predOtp)

'''
 Predict on the basis of the policy Lookup Table
'''
def predict_(P, inp):

    for p in P:
        find = np.where(np.all(p[0] == inp, axis=0))
        if len(find[0]):
            return p[1]
            break

def format(inp):
    inp = ['x' if x == 1 else x for x in inp]
    inp = ['o' if x == -1 else x  for x in inp]
    inp = ['_' if x == 0 else x  for x in inp]

    print inp[0], inp[1], inp[2]
    print inp[3], inp[4], inp[5]
    print inp[6], inp[7], inp[8]


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("--ann", action="store_true", default=False, dest="ann", help="Play using tehe trained Neural Network")

    parser.add_argument("--lookup", action="store_true", default=True, dest="lookup", help="Play using the lookup table")

    result = parser.parse_args()
    f = open('policy.bin', 'rb')
    P = np.load(f)


    with open('ann.pickle', 'rb') as handler:
        weight = pickle.load(handler)

        for p in P:
            print predict_(P, p[0])-predict(weight, p[0])
    #
    #     grid = [0]*9
    #     while True:
    #
    #         if result.ann:
    #             grid = predict(weight, grid)
    #         elif result.lookup:
    #             grid = predict_(P, grid)
    #         format(grid)
    #
    #         hasEnd = board.hasEnd(grid)
    #         if hasEnd[0]:
    #             print hasEnd[1], " won!!"
    #             break
    #
    #         row = input("Row: ")
    #         col = input("Coloumn: ")
    #
    #         grid[(row-1)*3 + col-1] = -1
    #         hasEnd = board.hasEnd(grid)
    #         print "--------------------------------"
    #         if hasEnd[0]:
    #             print hasEnd[1], " won!!"
    #             print "--------------------------------"
    #             break
