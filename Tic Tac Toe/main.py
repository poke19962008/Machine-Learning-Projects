import numpy as np
import board

def train(board):
    initState = np.zeros(9)
    frontier = board.nextStates(initState)
    path = [initState]

    while len(frontier):
        nextLevel = []

        for i in xrange(0, len(frontier)):
            nextMove = board.nextStates(frontier[i])

            for j in xrange(0, len(nextMove)):
                # if board.hasWin(nextMove[j])[0]:
                    # do back propagation

                np.append(nextLevel, nextMove[j], axis=0)


if __name__ == '__main__':
    boards = board.combinations()
    train(board)
