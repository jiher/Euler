#!/usr/bin/python
## euler 78
# trouver n tel que 1 000 000 divise p(n)

def pentagonal(n):
    if n%4==3 or n%4==0: sgn=-1
    else: sgn =1 
    return((3*n-1)*n/2*sgn)
    
global partitions=[]
partitions[0]=1

for i in range(1,10): print pentagonal(i)
