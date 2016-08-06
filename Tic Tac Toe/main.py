import numpy as np
import board

def train(boards):
    initState = np.zeros(9)
    player = 'o'
    stack = np.array([initState])
    visited = np.empty((0, 9), int)

    while len(stack):
        curState = stack[len(stack)-1]
        player = 'o' if player == 'x' else 'x'
        nextMove = board.nextStates(curState, player)
        visited = np.append(visited, [curState], axis=0)
        # print curState

        counter = 0
        for i in xrange(0, len(nextMove)):
            counter += 1
            # Check if the match is won/draw
            # if nextMove[i] not in visited:
                # stack = np.append(stack, [nextMove[i]], axis=0)
                # break

        if counter == len(nextMove):
            np.delete(stack, 0)


if __name__ == '__main__':
    boards = board.combinations()
    train(board)
    # board.hasWin([1, 1, 1, -1, -1, 0, 0, 0, 0])
