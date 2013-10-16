#!/usr/bin/env python3


def pentagonal(n):
    """ retourne un tableau avec nos pentagonaux généralisés"""
    result=[]
    for i in range(-n,n+1):
      result.append(abs(int(i * (3 * i - 1) / 2)))
    result.sort()
    
    for i in range(len(result)):
        if i%4==0 or i%4==3: result[i]=-result[i]
    result = result[1:]
    return result



def parti(n,coefs):
    pass

penta=pentagonal(20)
print(penta)


