## Neural Networks Assignment (CS1104)

### Model 1

This model consist of only NAND gates arranged in suitable order. Below shows the logic diagram of the circuit.

<center>![](https://upload.wikimedia.org/wikipedia/commons/f/fa/XOR_from_NAND.svg)</center>

This network executed all the 4 test cases in **0.036s**, with error of 0%.

### Model 2

This model consist of only NOR gates arranged in suitable order. Below shows the logic diagram of the circuit.

<center>![](https://upload.wikimedia.org/wikipedia/commons/e/e3/XOR_from_NOR.svg)</center>

This network executed all the 4 test cases in **0.003s**, with error of 0%.

### Model 3

This model consist of NAND, AND and OR gates arranged in suitable order. Below shows the logic diagram of the circuit.

<center>![](https://upload.wikimedia.org/wikipedia/commons/a/a2/254px_3gate_XOR.jpg)</center>

This network executed all the 4 test cases in **0.003s**, with error of 0%.


## How to run

```bash
$ g++ main.cpp --std=c++11
$ ./a.out 
```