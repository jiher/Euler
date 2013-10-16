#!/usr/bin/env python
MAX=30
t1=[1]*MAX
#t0=[0]*MAX
def mult(t1,t2):
    res=[0]*(len(t1)+len(t2))
    for i in range(len(t1)):
        for j in range(len(t2)):
            res[i+j]+= t1[i]*t2[j]
    return res
def polypuissance(n):
    res=[0]*MAX
    res[0]=1
    for i in range(1,MAX):
        if i%n==0:
            res[i]=1
    return res
prod=t1
for i in range(2,MAX):
    poly_puissance=polypuissance(i)
    
    prod=mult(prod,poly_puissance)
print i,prod,poly_puissance