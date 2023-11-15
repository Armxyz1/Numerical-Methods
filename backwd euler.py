from math import *

def fixed_pt(x0,g,N,tol):
    x=x0
    i=1
    while i<=N:
        x=g(x)
        if abs(x-g(x))<tol:
            return x
        i+=1
    return x

def bkwdeuler(a,alpha,h,f,N):
    w0=alpha
    for i in range(N):
        x=a+i*h
        g=lambda w:w0+h*f(x+h,w)
        w0=fixed_pt(w0,g,100,1e-5)
    return w0