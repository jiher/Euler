#!/usr/bin/python

## Euler 131

"""
Theoreme de Lucas 
c(n,p)%q 
"""
def erato(nbr):                #crible d'eratosthene
    premier=range(3,nbr,2)     #retourne la liste des
    long=len(premier)          #nombres premiers inferieurs a "nbr"
    i=0
    next=3
    fin=int(math.sqrt(float(nbr)))+1
    while next<fin:
        j=i+next
        while j<long:
            premier[j]=0 #met a 0 les multiples de next
            j=j+next
        i=i+1
        while  (premier[i]==0):
                        i=i+1
        next =premier[i] #Le nombre premier suivant
        
    premier=filter(None,premier) #enleve les termes nuls du tableau
    return premier
max=1000000
import math 
borne =int(math.sqrt(max))
primes=erato(1000000)
resul=[]

def en_base(n,b):
    # retourne l'ecriture du nombre n>1 en base b>=2
    result=[]
    p=1
    result.append(n%b)
    while p<n:
        p=*b
        (q,r)=divmod(n,p)
        result.append(q)
    return result
for (n,b) in ((10,2),(10,3)(1024,16):

    print n,b,en_base(n,b)