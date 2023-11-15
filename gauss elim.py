from math import *

def gauss_elim(A,B,n):
    for i in range(n):
        for j in range(n):
            if A[i][j]!=0:
                p=j
                break
        for j in range(n):
            A[i][j],A[p][j]=A[p][j],A[i][j]
        B[i][0],B[p][0]=B[p][0],B[i][0]
        for j in range(i+1,n):
            m=A[j][i]/A[i][i]
            for k in range(n):
                A[j][k]-=m*A[i][k]
            B[j][0]-=m*B[i][0]
    x=[[0] for i in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(n-1,i,-1):
            B[i][0]-=A[i][j]*x[j][0]
        x[i][0]=B[i][0]/A[i][i]
    return x
