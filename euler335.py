#!/usr/bin/python




def move(start,board,TAILLE):
    long=board[start]
    board[start]=0
    for i in range(long):
        board[(start+i+1)%TAILLE]+=1
           
    current=(long+start)%TAILLE
    return(board,current)



def resolve(board,TAILLE,current=0):
    cpt=0
    while True:
        (board,current)=move(current,board,TAILLE)
        cpt+=1
        if board== [1]*TAILLE:
            # print TAILLE,cpt
            
            return(cpt)
current=0
cpt=0
result=[]
for TAILLE in range(2,300):
    board=[1]*TAILLE    
    cpt=resolve(board,TAILLE,0)
    print TAILLE,cpt
    result.append(cpt)

print result
for i in range(1,len(result)):
    print i+1,result[i-1],result[i]-result[i-1]


