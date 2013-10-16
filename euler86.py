import math

def test_pythagore(M):
  res=[0]
  i=1
  while i<=M:
    if math.sqrt(M*M+i*i)==int(math.sqrt(M*M+i*i)):
      res.append( i)
    i+=1
  return res

def gen_triplets(M):
  """ genere les triplets a<=b<=c=<M"""
  res=[]
  for a in range(1,M):
      for b in range(1,a+1):
	for c in range(1,b+1):
	  res.append((a,b,c))
  return res
  
def mindist(c):
    (a,b,c)=c
    s1=(a+b)*(a+b)+c*c
    s2=b*b+(a+c)*(a+c)
    s3=a*a+(c+b)*(c+b)
    return min(s1,s2,s3)


if __name__=='__main__':
  M=350
  final=0
  for i in range(1,M):
    tmp=test_pythagore(i)
    if len(tmp)==1: continue
    for n in tmp[1:]:
      if n%2: final+=n/2
      else:final+=(n+1)/2
    print i,final,tmp
  """cuboides=gen_triplets(M)
  print len(cuboides)
  count=0
  for c in cuboides :
    mind=mindist(c)
    if  math.sqrt(mind) == int(math.sqrt(mind)): 
      print c,mind
      count +=1
      
  print count"""