import board
import numpy as np
import pickle
import argparse

'''
 Predict on the basis of given Neural Network model
'''
def predict(model, inp):
    inp = np.array(inp)
    W1, W2, B1, B2 = model["W1"], model["W2"], model["B1"], model["B2"]

    Z1 = inp.dot(W1) + B1
    a1 = np.tanh(Z1)
    Z2 = a1.dot(W2)  + B2
    predOtp = np.tanh(Z2)

    return predOtp

'''
 Predict on the basis of the policy Lookup Table
'''
def predict_(inp):
    f = open('policy.bin', 'rb')
    P = np.load(f)

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

    with open('ann.pickle', 'rb') as handler:
        model = pickle.load(handler)

        grid = [0]*9
        while True:

            if result.ann:
                grid = predict(model, grid)[0]
                grid = np.around(grid)
            elif result.lookup:
                print "herer"
                grid = predict_(grid)
            format(grid)

            hasEnd = board.hasEnd(grid)
            if hasEnd[0]:
                print hasEnd[1], " won!!"
                break

            row = input("Row: ")
            col = input("Coloumn: ")

            grid[(row-1)*3 + col-1] = -1
            hasEnd = board.hasEnd(grid)
            print "--------------------------------"
            if hasEnd[0]:
                print hasEnd[1], " won!!"
                print "--------------------------------"
                break