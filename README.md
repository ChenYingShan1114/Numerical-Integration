
# Numerical Integration
## Reference
A. L. Garcia, "Numerical Methods for Physics": \ 
Chapter 10 Special Functions and Quadrature
## Exercisies
### 10-1.Bessel
The second solution to Bessel’s equation is $Y_m(x)$, the Bessel function of the second kind. Write a function to compute $Y_m(x)$ using upward recursion
```math
Y_{m+1}=\frac{2m}{x}Y_m(x)-Y_{m-1}(x)
```
To obtain the starting values for recursion, use the identities
```math
Y_0(x)=\frac{2}{\pi} \left[ ln{\frac{x}{2}} + \gamma \right] J_0(x) - \frac{4}{\pi} \sum_{k=1}^\infty (-1)^k \frac{J_{2k}(x)}{k}
```
and
```math
J_1(x)Y_0(x)-J_0(x)Y_1(x)=\frac{2}{\pi x}
```
where $\gamma \approx 0.577215664$. Demonstrate your routine by producing plots of $Y_m(x)$ for $0$ $<$ $x$ $<$ $50$ and various $m$.
### 10-2.Richardson
Richardson extrapolation can be used to improve our formulas for estimating derivatives. Take the centered first derivative approximation,
```math
D_{i,1} = \frac{f(x+h_i) - f(x-h_i)}{2h_i} = f'(x) + O(h_i^2)
```
with $h_{i+1}=0.5h_i$ and define the Richardson extrapolation
```math
D_{i+1,j+1} = D_{i+1,j} + \frac{1}{4^j-1}(D_{i+1,j}-D_{i,j})
```
(a) Using Taylor expansion show that  $|f'(x)-D_{i,2}|=O(h_i^4)$. \
(b) Write a function, similar to  **rombf.cpp**, that computes the Richardson extrapolation table for derivatives. Test the function by graphing $|f'(x)-D_{i,2}|$ and $|f'(x)-D_{i,i}|$ versus $i$ for $f(x)=e^x$ at $x=10$ taking $h_1=1$.

### 10-3.partical-in-can
(a) Write a program to find the shift in the ground state energy for the perturbed particle in a can [see Equation (10.85)]. Use Gaussian quadrature to evaluate the integral for $\gamma=0.5$, $1$, $2$, $3$, and $4$. \
(b) Repeat part (a) using the perturbation $V'(r)=V'_c \left| \frac{x}{R} \right|^\gamma$ for  $\gamma=1$, $2$, $3$, and $4$.
