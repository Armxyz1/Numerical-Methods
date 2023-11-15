from math import *
def deteminant(A,n):
    if n == 1:
        return A[0][0]
    elif n == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    else:
        det = 0
        for i in range(n):
            det += ((-1)**i)*A[0][i]*deteminant(minor(A,0,i),n-1)
        return det
def minor(A,i,j):
    return [row[:j] + row[j+1:] for row in (A[:i]+A[i+1:])]
def cofactor(A,n):
    return [[((-1)**(i+j))*deteminant(minor(A,i,j),n-1) for j in range(n)] for i in range(n)]
def transpose(A,n):
    return [[A[j][i] for j in range(n)] for i in range(n)]
def inverse(A,n):
    det = deteminant(A,n)
    if det == 0:
        return None
    elif n==1:
        return [[1/det]]
    elif n==2:
        return [[A[1][1]/det,-A[0][1]/det],[-A[1][0]/det,A[0][0]/det]]
    else:
        cofactors=[]
        for i in range(n):
            cofactorsRow=[]
            for j in range(n):
                cofactorsRow.append(deteminant(minor(A,i,j),n-1)*((-1)**(i+j)))
            cofactors.append(cofactorsRow)
        cofactors=transpose(cofactors,n)
        for i in range(n):
            for j in range(n):
                cofactors[i][j]/=det
        return cofactors
def solve(A,B,N):
    """
    Gaussian elimination
    """
    for i in range(N):
        for j in range(N):
            if A[i][j]!=0:
                p=j
                break
        if p!=i:
            for j in range(N):
                A[i][j],A[p][j]=A[p][j],A[i][j]
            B[i],B[p]=B[p],B[i]
        for j in range(i+1,N):
            c=A[j][i]/A[i][i]
            for k in range(N):
                A[j][k]-=c*A[i][k]
            B[j]-=c*B[i]
    X=[0 for i in range(N)]
    X[N-1]=B[N-1]/A[N-1][N-1]
    for i in range(N-2,-1,-1):
        sum=0
        for j in range(i+1,N):
            sum+=A[i][j]*X[j]
        X[i]=(B[i]-sum)/A[i][i]
    return X
def multiply(A,B,p,q,r):
    C=[[0 for i in range(r)] for j in range(p)]
    for i in range(p):
        for j in range(r):
            for k in range(q):
                C[i][j]+=A[i][k]*B[k][j]
    return C
def norm(A,n):
    """
    Frobenius norm
    """
    sum=0
    for i in range(n):
        for j in range(n):
            sum+=A[i][j]**2
    return sqrt(sum)
def add(A,B,p,q):
    C=[[0 for i in range(q)] for j in range(p)]
    for i in range(p):
        for j in range(q):
            C[i][j]=A[i][j]+B[i][j]
    return C
def subtract(A,B,p,q):
    C=[[0 for i in range(q)] for j in range(p)]
    for i in range(p):
        for j in range(q):
            C[i][j]=A[i][j]-B[i][j]
    return C
def identity(n):
    A=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        A[i][i]=1
    return A

