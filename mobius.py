#!/usr/bin/python


""" sur le principe d'eratosthene, crecron un tableau avec les valeur de la fonction de mobius"""


max=10000000

def mob(max):
""" fonction de mobius etendue
    mobs{n]=0=> n premier
            -1=> n contient un carre
            m>0: nombre de diviseur distinct de N
    on retrouve facilement les valeur de la fonction de mobius
    mu(n)=0 si mobs[n]=-1
    mu(n)= 1 si mobs[n]%2 ==0
    mu(n)=-1 si mobs[n]%2==1
    
    """
    
    mobs=[0]*max ## tout les nombres sont crees premier
    mobs[0]=-1
    mobs[1]=-1
    for i in range(2,max):
        if mobs[i]==-1: continue
        if mobs[i]==0:
            carre=i*i
            for tmp in range(i+i,max,i):
                if tmp%carre==0 or mobs[tmp]==-1: 
                    mobs[tmp]=-1 ## le nombre contient un carre    
                else:
                    mobs[tmp]+=1
    return mobs
mobs=mob(max)     
m=1
imax=1
for i in range(max):
    if mobs[i]>m:
        imax=i
        m=mobs[i]
print imax,m