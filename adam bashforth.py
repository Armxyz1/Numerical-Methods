from math import *

a=0
alpha=0
def adam_bash_2(a,alpha,h,f,N):
    w0=alpha
    k1=h*f(a,w0)
    k2=h*f(a+h/2,w0+k1/2)
    w1=w0+(k1+k2)/2
    for i in range(1,N):
        x=a+i*h
        w2=w1+h/2*(3*f(x,w1)-f(x-h,w0))
        w0=w1
        w1=w2
    return w1

def adam_bash_3(a,alpha,h,f,N):
    w0=alpha
    k1=h*f(a,w0)
    k2=h*f(a+h/2,w0+k1/2)
    k3=h*f(a+h,w0-k1+2*k2)
    w1=w0+(k1+4*k2+k3)/6
    a=a+h
    k1=h*f(a,w1)
    k2=h*f(a+h/2,w1+k1/2)
    k3=h*f(a+h,w1-k1+2*k2)
    w2=w1+(k1+4*k2+k3)/6
    for i in range(2,N):
        x=a+i*h
        w3=w2+h/12*(23*f(x,w2)-16*f(x-h,w1)+5*f(x-2*h,w0))
        w0=w1
        w1=w2
        w2=w3
    return w2

def adam_bash_4(a,alpha,h,f,N):
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
    a=a+h
    k1=h*f(a,w2)
    k2=h*f(a+h/2,w2+k1/2)
    k3=h*f(a+h/2,w2+k2/2)
    k4=h*f(a+h,w2+k3)
    w3=w2+(k1+2*k2+2*k3+k4)/6
    for i in range(3,N):
        x=a+i*h
        w4=w3+h/24*(55*f(x,w3)-59*f(x-h,w2)+37*f(x-2*h,w1)-9*f(x-3*h,w0))
        w0=w1
        w1=w2
        w2=w3
        w3=w4
    return w4