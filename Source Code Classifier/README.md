# Source Code Classifier

Naive Bayes approach for classifing programming language (i.e. python, java, C++, C, Ruby) from the given source code.

## Feature 

Feature consist of frequency of RegEx (`reStore.py`) marker matches from the given source code. Markers are manually handpicked from various languages.



## Probability Distribution of Markers of Languages

Graph below shows the probability of the markers for a given programming language during the training phase. Note that for every language the activation of markers consist of fixed range. Actual range of markers are show below:

- Python Marker: 0-44
- C Marker: 45-54
- C++ Marker: 55-92
- Java Marker: 93-107
- Ruby Markers: 108-115

![Probability Distribution](https://raw.githubusercontent.com/poke19962008/Machine-Learning-Projects/master/Source%20Code%20Classifier/plot/markerProbabilty.png)


To make everything more clear here is the Normalised Probility Distribution Functio for every programming language.

![Probability Distribution](https://raw.githubusercontent.com/poke19962008/Machine-Learning-Projects/master/Source%20Code%20Classifier/plot/normDist.png)


## Result

 - Length of Test Datasets: 4102
 - Length of Validation Datasets: 1758
 - Number of features: 115
 - Accuracy over Validation Set: 99.03%