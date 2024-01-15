#include <iostream>
#include <fstream>
#include <assert.h>
#include <math.h>
#include "Matrix.h"
using namespace std;

double func( double x) {
  return exp(x);
}

int main(){

    double x = 10, h = 2;
    int N = 20;
    Matrix D(N, N);
    for (int i = 1; i <= N; i++){
        h = h / 2;
        D(i, 1) = (func(x+h) - func(x-h)) / 2 / h;
    }
    for (int i = 2; i <= N; i++){
        for (int j = 2; j <= i; j++){
            D(i, j) = D(i, j-1) + (D(i, j-1) - D(i-1, j-1)) / (pow(4, j-1) - 1);
        }
    }
    for (int i = 1; i <= N; i++){
        for (int j = 1; j <= i; j++){
            cout << D(i, j) << " ";
        }
        cout << endl;
    }

    Matrix error1(N), error2(N);
    for (int i = 1; i <= N; i++){
        error1(i) = abs(func(10) - D(i, 1));
        error2(i) = abs(func(10) - D(i, i));
    }

    ofstream error1Out("error1out.txt"), error2Out("error2out.txt");
    for (int i = 1; i <= N; i++){
        error1Out << error1(i) << endl;
        error2Out << error2(i) << endl;
    }    
    
}
