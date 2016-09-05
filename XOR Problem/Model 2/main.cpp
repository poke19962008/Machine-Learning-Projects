#include <iostream>
#include "xor.h"
using namespace std;

int main(int argc, char const *argv[]) {

  XOR obj;

  cout<<"Testing: ";
  obj.test();

  bool a, b;

  cout<<"Enter A: "; cin>>a;
  cout<<"Enter B: "; cin>>b;
  cout<<"A^B: "<<obj.compute(a, b);

  return 0;
}
