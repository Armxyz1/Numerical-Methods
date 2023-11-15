from math import *

def predictor(a,alpha,h,f,N):
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
        w_bad=w3+h/24*(55*f(x,w3)-59*f(x-h,w2)+37*f(x-2*h,w1)-9*f(x-3*h,w0))
        w4=corrector(w1,w2,w3,w_bad,h,x,f)
        w0=w1
        w1=w2
        w2=w3
        w3=w4
    return w3
def corrector(a0,a1,a2,a3,h,x,f):
    return a2+h/24*(9*f(x+h,a3)+19*f(x,a2)-5*f(x-h,a1)+f(x-2*h,a0))