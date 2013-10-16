#!/usr/bin/python

def residus(n):
     res=[]
     for i in range(n):
          res.append( i*i%n)
     return res
          

if __name__=='__main__':
     for i in range(11):
          print residus(i)
     