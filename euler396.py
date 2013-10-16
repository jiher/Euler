#!/usr/bin/python

base=2
nbre=[1,1,0,0]

while nbre <>[0,1,0,0]:
 
    base+=1

    if nbre[3]>0:
        nbre[3]-=1
    else:
        print base,nbre
        nbre[3]=base-1   
        if nbre[2]>0:
            nbre[2]-=1
        else:
            print base,nbre
            nbre[2]=base-1
            if nbre[1]>0:
                nbre[1]-=1
            else:
                nbre[0]-=1
                nbre[1]=base-1
    
print  base -2
