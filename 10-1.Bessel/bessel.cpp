#include <iostream>
#include <fstream>
#include <assert.h>
#include <math.h>
#include "Matrix.h"
using namespace std;
#include "bess.h"

int main(){

    double gamma = 0.577215664, pi = 3.1415926;
    int N = 250;
    Matrix x(N);
    Matrix Y0(N), Y1(N), J0(N), J1(N);
    int k = 30, m = 2 * k;
    Matrix J_tmp(m+1);
    double tmp = 0;
    for (int i = 1; i <= N; i++){
        x(i) = (i - 0.5) * 0.2;
        tmp = 0;
        J_tmp.set(0.0);
        bess(m, x(i), J_tmp);
        for (int j = 1; j <= k; j++){
            tmp = tmp + 4 / M_PI * pow(-1, j) * J_tmp(2*j+1) / j;
        }
        J0(i) = J_tmp(1);
        J1(i) = J_tmp(2);
        Y0(i) = 2 / M_PI * (log(x(i) / 2) + gamma) * J_tmp(1) - tmp;
        Y1(i) = (J1(i) * Y0(i) - 2 / M_PI / (x(i) + 1e-16)) / J0(i);
    }

    m = 10;
    Matrix Y(N, m);
    for (int i = 1; i <= N; i++){
        Y(i, 1) = Y0(i);
        Y(i, 2) = Y1(i);
        for (int j = 2; j <= m-1; j++){
            Y(i, j+1) = 2 * (j - 1) / (x(i) + 1e-16) * Y(i, j) - Y(i, j-1);
        }
    }

    ofstream XOut("Xout.txt"), YOut("Yout.txt");
    for (int i = 1; i <= N; i++){
        XOut << x(i) << endl;
    }
    for (int j = 1; j <= m; j++){
        for (int i = 1; i < N; i++){
            YOut << Y(i, j) << ", ";
        }
        YOut << Y(N, j) << endl;
    }

}
