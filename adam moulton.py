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

def adam_moulton_2(a,alpha,h,f,N):
    w0=alpha
    k1=h*f(a,w0)
    k2=h*f(a+h/2,w0+k1/2)
    k3=h*f(a+h,w0-k1+2*k2)
    w1=w0+(k1+k2)/2
    for i in range(1,N):
        x=a+i*h
        g=lambda w:w1+h/12*(5*f(x+h,w)+8*f(x,w1)-f(x-h,w0))
        w2=fixed_pt(w1,g,100,1e-5)
        w0=w1
        w1=w2
    return w1

def adam_moulton_3(a,alpha,h,f,N):
    w0=alpha
    k1=h*f(a,w0)
    k2=h*f(a+h/2,w0+k1/2)
    k3=h*f(a+h/2,w0+k2/2)
    k4=h*f(a+h,w0+k3)
    w1=w0+(k1+2*k2+2*k3+k4)/6
    a=a+h
    k1=h*f(a,w1)
    k2=h*f(a+h/2,w1+k1/2)
    k3=h*f(a+h/2,w1+k2/2)
    k4=h*f(a+h,w1+k3)
    w2=w1+(k1+2*k2+2*k3+k4)/6
    for i in range(2,N):
        x=a+i*h
        g=lambda w:w2+h/24*(9*f(x+h,w)+19*f(x,w2)-5*f(x-h,w1)+f(x-2*h,w0))
        w3=fixed_pt(w2,g,100,1e-5)
        w0=w1
        w1=w2
        w2=w3
