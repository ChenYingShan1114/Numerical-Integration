#include <iostream>
#include <fstream>
#include <assert.h>
#include <math.h>
#include "Matrix.h"
using namespace std;
#include "bess.h"
#include "zeroj.h"

double eta01 = zeroj(0, 1);
//double gam = 3; // 0.5, 1, 2, 3, 4
double Vc = 1, R = 1;

double func(double x, double gamma){
    Matrix J_tmp(1);
    bess(0, eta01 * (x+1) / 2, J_tmp);
    double J0 = J_tmp(1);
    return pow(0.5*R, gamma+2) * pow(x+1, gamma+1) * J0 * J0;
}

double cos_func(double x, double gam){
    return pow(cos(M_PI / 4 * (1 + x)), gam) * M_PI;
}

int main(){

    Matrix J_tmp(2);
    bess(1, eta01, J_tmp);
    double J1 = J_tmp(2);
    
    Matrix gam(5);
    gam(1) = 0.5; gam(2) = 1; gam(3) = 2; gam(4) = 3; gam(5) = 4;
    double w1 = 5.0/9.0, w2 = 8.0/9.0, w3 = 5.0/9.0;
    double x1 = -sqrt(3.0/5.0), x2 = 0.0, x3 = sqrt(3.0/5.0);
    for (int i = 1; i <= 5; i++){
        double gamma = gam(i);
        double result_rho = 0, result_x = 0;
        result_rho = w1 * func(x1, gamma) + w2 * func(x2, gamma) + w3 * func(x3, gamma);
        result_rho = 2 * Vc / pow(R, gamma+2) / J1 / J1 * result_rho;
        result_x = result_rho * (w1 * cos_func(x1, gamma) + w2 * cos_func(x2, gamma) + w3 * cos_func(x3, gamma)) / 2 / M_PI;
        cout << "gamma = " << gamma << endl;
        cout << "energy(rho) = " << result_rho << endl;
        cout << "energy(x) = " << result_x << endl;
    }
}
