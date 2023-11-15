from math import *

def rk4(a,alpha,h,f,N):
    w0=alpha
    for i in range(N):
        x=a+i*h
        k1=f(x,w0)
        k2=f(x+h/2,w0+h/2*k1)
        k3=f(x+h/2,w0+h/2*k2)
        k4=f(x+h,w0+h*k3)
        w0=w0+h/6*(k1+2*k2+2*k3+k4)
    return w0

def rk2fwd(a,alpha,h,f,N):
    w0=alpha
    for i in range(N):
        x=a+i*h
        k1=h*f(x,w0)
        k2=h*f(x+h,w0+k1)
        w0=w0+1/2*(k1+k2)
    return w0

def rk2mid(a,alpha,h,f,N):
    w0=alpha
    for i in range(N):
        x=a+i*h
        k1=h*f(x,w0)
        k2=h*f(x+h/2,w0+k1/2)
        w0=w0+k2
    return w0

def heun(a,alpha,h,f,N):
    w0=alpha
    for i in range(N):
        x=a+i*h
        k1=h*f(x,w0)
        k2=h*f(x+2/3*h,w0+2/3*k1)
        w0=w0+1/4*k1+3/4*k2
    return w0

def rk3(a,alpha,h,f,N):
    w0=alpha
    for i in range(N):
        x=a+i*h
        k1=h*f(x,w0)
        k2=h*f(x+h/2,w0+k1/2)
        k3=h*f(x+h,w0-k1+2*k2)
        w0=w0+1/6*(k1+4*k2+k3)
    return w0