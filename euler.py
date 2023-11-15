from math import *

def f(x, y):
    pass
def euler(a,alpha,h,f,N):
    w0=alpha
    for i in range(N):
        x=a+i*h
        w0=w0+h*f(x,w0)
    return w0
