from math import *
import numpy as np

n=
a=
alpha=np.array([])
def  F(t,w):
    return np.array([])
def rk2multi(a,alpha,h,N,F):
    w0=alpha
    for i in range(N):
        t=a+i*h
        k1=h*F(t,w0)
        k2=h*F(t+h/2,w0+k1/2)
        w0=w0+k1/2+k2/2
    return w0
print(rk2multi(a,alpha,h,n,F))