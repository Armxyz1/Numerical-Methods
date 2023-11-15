from math import *
from matrix_functions import *
def lin_finite_diff(a,b,alpha,beta,N,p,q,r):
    h=(b-a)/(N+1)
    x=[a+i*h for i in range(N+2)]
    A=[[0 for i in range(N)] for j in range(N)]
    B=[[0] for i in range(N)]
    for i in range(1,N+1):
        A[i-1][i-1]=-(2+h**2*q(x[i]))
        if i!=1:
            A[i-1][i-2]=1+h/2*p(x[i])
        if i!=N:
            A[i-1][i]=1-h/2*p(x[i])
        B[i-1][0]=h**2*r(x[i])
    B[0][0]-=(1+h/2*p(x[1]))*alpha
    B[N-1][0]-=(1-h/2*p(x[N]))*beta
    y=solve(A,B,N)
    return x[1:N+1],y


