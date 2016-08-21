/* -*- C++ -*- */

#include <iostream>
#include <array>
#include <ctime>
using namespace std;

const int tSetLen = 4;

class XOR {
private:
  int trainingSet[tSetLen][3] = {{0, 0, 0}, {0, 1, 1}, {1, 0, 1}, {1, 1, 0}};

public:

  int nandNeuron(int x1, int x2){
    const int bias = 3;
    const int weight = -2;

    int Yin = x1*weight + x2*weight + bias;
    return (Yin > 0)? 1:0;
  }

  int compute(int x1, int x2){
    int A1 = nandNeuron(x1, x2);
    int B1 = nandNeuron(A1, x1);
    int B2 = nandNeuron(A1, x2);
    int C1 = nandNeuron(B1, B2);

    return C1;
  }

  void test(){
    int correct = 0;

    cout<<"Starting test over "<<tSetLen<<" test cases."<<endl;
    int start_s=clock();
    for (size_t i = 0; i < tSetLen; i++) {
      int hyp = compute(trainingSet[i][0], trainingSet[i][1]);
      if(hyp == trainingSet[i][2]) correct++;
    }

    cout<<"Model Analysis\nAccuracy: "<<(float)(correct/tSetLen)*100<<"\%\n";
    cout<<"Error: "<<(float)(1-correct/tSetLen)*100<<"\%\n";
    int stop_s=clock();
    cout<<"Total Time: " << (stop_s-start_s)/double(CLOCKS_PER_SEC)*1000 << endl;

  }

};
