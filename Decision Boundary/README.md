# Decision Boundary

Boundary decisions, or edge effects, refer to the problem of deciding whether to include plants intersected by the sample unit boundary. Boundary decisions are more frequently encountered in vegetation with abundant plant populations, and are a less significant issue when sampling areas with sparse plant abundance.

### Architecture

It consist of 3 layered Neural Network. One inpult layer with 2 node for x and y coordinates, hidden layer consist variable nodes and output layer consist of 2 probabilty for class A or B

![alt text](https://github.com/poke19962008/Neural-Network-Projects/blob/master/Decision%20Boundary/res/netArch.png?raw=true "Architecture")

## Working

Have used `hyperbolic tangent` as the activation function for the hidden layer `Z1` and `softmax` for converting the raw scores from the hidden layer to probabilities. Weight adjustments have been made by minimising `Mean Square Error` of the neural network by using `Batch Gradient Descent` algorithm with constant learning rate. To calculate the gradients I have used `Back Propogation` algorithm.

![alt text](https://github.com/poke19962008/Neural-Network-Projects/blob/master/Decision%20Boundary/res/CodeCogsEqn.png?raw=true "LaTeX")

## Output

![alt text](https://github.com/poke19962008/Neural-Network-Projects/blob/master/Decision%20Boundary/figure_1.png?raw=true "Architecture")
