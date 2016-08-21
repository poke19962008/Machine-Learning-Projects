/* -*- C++ -*- */

#include <iostream>
#include <array>
#include <ctime>
using namespace std;

const int tSetLen = 4;

class XOR {
private:
  int testSet[tSetLen][3] = {{0, 0, 0}, {0, 1, 1}, {1, 0, 1}, {1, 1, 0}};

public:
  int stepFunction(int x) {
    return (x >= 0)? 1:0;
  }

  int nandNeuron(int x1, int x2){
    const int bias = 3;
    const int weight = -2;

    int Yin = x1*weight + x2*weight + bias;
    return stepFunction(Yin);
  }

  int andNeuron(int x1, int x2){
    const int bias = -3;
    const int weight = 1;

    int Yin = x1*weight + x2+weight + bias;
    return stepFunction(Yin);
  }

  int orNeuron(int x1, int x2){
    const int bias = -2;
    const int weight = 1;

    int Yin = x1*weight + x2+weight + bias;
    return stepFunction(Yin);
  }

  int compute(int x1, int x2){
    int A1 = nandNeuron(x1, x2);
    int A2 = orNeuron(x1, x2);

    int B1 = andNeuron(A1, A2);
    return B1;
  }

  void test(){
    int correct = 0;

    cout<<"Starting test over "<<tSetLen<<" test cases."<<endl;
    int start_s=clock();
    for (size_t i = 0; i < tSetLen; i++) {
      int hyp = compute(testSet[i][0], testSet[i][1]);
      if(hyp == testSet[i][2]) correct++;
    }

    int stop_s=clock();
    cout<<"Model Analysis\nAccuracy: "<<(float)(correct/tSetLen)*100<<"\%\n";
    cout<<"Error: "<<(float)(1-correct/tSetLen)*100<<"\%\n";
    cout<<"Total Time: " << (stop_s-start_s)/double(CLOCKS_PER_SEC)*1000 << endl;

  }

};
