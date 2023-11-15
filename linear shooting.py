from math import *

y1=[]
y1_prime=[]
y2=[]
y2_prime=[]
w1=[]
w2=[]
def linear_shooting(a,alpha,beta,h,N,p,q,r):
    y1.append(alpha)
    y1_prime.append(0)
    y2.append(0)
    y2_prime.append(1)
    u1=alpha
    u1_prime=0
    u2=0
    u2_prime=1
    for i in range(N):
        x=a+i*h
        u1=u1+h*u1_prime
        u1_prime=u1_prime+h*(p(x)*u1_prime+q(x)*u1+r(x))
        u2=u2+h*u2_prime
        u2_prime=u2_prime+h*(p(x)*u2_prime+q(x)*u2)
        y1.append(u1)
        y1_prime.append(u1_prime)
        y2.append(u2)
        y2_prime.append(u2_prime)
    w10=alpha
    w20=(beta-y1[N])/y2[N]
    w1.append(w10)
    w2.append(w20)
    for i in range(N+1):
        w1.append(y1[i]+w20*y2[i])
        w2.append(y1_prime[i]+w20*y2_prime[i])
    return w1,w2