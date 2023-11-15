from math import *

def f(x, y):
    pass
def f_x(x, y):
    pass
def f_y(x, y):
    pass
def taylor(a,alpha,h,f,N):
    w0=alpha
    for i in range(N):
        x=a+i*h
        w0=w0+h*f(x,w0)+h**2/2*(f_x(x,w0)+f(x,w0)*f_y(x,w0))
    return w0