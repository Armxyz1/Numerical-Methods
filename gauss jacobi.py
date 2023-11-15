from math import *
from matrix_functions import *
def gauss_jacobi(A,B,n,TOL):
    x0=[0]*n
    x1=[0]*n
    while True:
        for i in range(n):
            x1[i]=B[i][0]
            for j in range(n):
                if i!=j:
                    x1[i]-=A[i][j]*x0[j]
            x1[i]/=A[i][i]
        if max([abs(x1[i]-x0[i]) for i in range(n)])/max([abs(i) for i in x1])<=TOL:
            break
        x0=x1.copy()
    return x1