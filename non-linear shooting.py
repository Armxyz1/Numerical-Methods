from math import *
import numpy as np

y=[]
y_prime=[]
def non_linear_shooting(a,b,alpha,beta,N,M,h,TOL,f,f_y,f_y_prime):
    t=(beta-alpha)/(b-a)
    k=1
    while k<=M:
        w10=alpha
        w20=t
        u1=0
        u2=1
        y[0]=w10
        y_prime[0]=w20
        for i in range(1,N+1):
            x=a+(i-1)*h
            y[i]=y[i-1]+h*y_prime[i-1]
            y_prime[i]=y_prime[i-1]+h*f(x,y[i-1],y_prime[i-1])
            u1=u1+h*u2
            u2=u2+h*(f_y(x,u1,u2)*u1+f_y_prime(x,u1,u2)*u2)
        if abs(y[N]-beta)<=TOL:
            return y
        t=t-(y[N]-beta)/u1
        k=k+1
    print("Method failed after",M,"iterations")