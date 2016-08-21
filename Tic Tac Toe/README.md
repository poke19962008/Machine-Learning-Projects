# Tic Tac Toe

Regular 3x3 1Player tic tac toe made using `Reinforcemnet Learning Algorithm`. Later the policy table has been feeded to 3 layered Convolution Neural Network to obtain pattern between state and action look up table.

## Learning

First I set uped all the possible states of game. Which corresponds to the probability of winning the game from that state. Probability is calculated using rewards `1 for winning`, `0.5 for draw` and `0 for loosing`. We play many games against opponent. To increase the accuracy I back up the value of state after each move. More precisely, the current value of the earlier state is adjusted to be closer to the value of the later state.

<center>![](https://raw.githubusercontent.com/poke19962008/Neural-Network-Projects/master/Tic%20Tac%20Toe/res/latex_a79dcf7bd9dbfae7dd6e1bd0825a2bb9.png)</center>

Where alpha is the Step Size Parameter, and its is reduced depending upon how many time that particular state has been visited.


To select the next moves I either applied greedy move or a random move. Decision is done on the basis of 	`epsilon` value. Greedy move is done by selecting the after state having highest probability. Si is the afterstates of S.

<center>![](https://raw.githubusercontent.com/poke19962008/Neural-Network-Projects/master/Tic%20Tac%20Toe/res/latex_22723d8bdae1422f06c3817903bd4b00.png)</center>

A sequence of tic-tac-toe moves. The solid lines represent the moves taken during a game; the dashed lines represent moves that we (our reinforcement learning player) considered but did not make. Our second move was an exploratory move, meaning that it was taken even though another sibling move, the one leading to e∗, was ranked higher. Exploratory moves do not result in any learning, but each of our other moves does, causing backups as suggested by the curved arrows and detailed in the text.

<center>![](https://raw.githubusercontent.com/poke19962008/Neural-Network-Projects/master/Tic%20Tac%20Toe/res/Screen%20Shot%202016-08-15%20at%206.05.41%20AM.png)</center>

## Artificial Neural Network

In order to reduce the computation speed and memory I have used Bidirectional Associative Memory (BAM) to store the look up table. Weight is calculated using

<center>![](https://raw.githubusercontent.com/poke19962008/Neural-Network-Projects/master/Tic%20Tac%20Toe/res/latex_66ac80c2437cfa38efe7a223a758ad40.png)</center> 

## Resources

- **Reinforcement Learning: An Introduction** by Richard S. Sutton and Andrew G. Barto

- **Artificial Intelligence: A Modern Approach** by Peter Norvig

- **Bidirectional Associative Memory (1988)** by Bart Kosko [[link]](http://sipi.usc.edu/~kosko/BAM.pdf)


- **Reinforcement Learning** by Andrew Ng [[watch]](https://www.youtube.com/watch?v=RtxI449ZjSc)