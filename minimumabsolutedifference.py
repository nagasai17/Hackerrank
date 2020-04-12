s=int(input())
k=list(map(int,input().split(" ")))
from itertools import permutations
k.sort()
l=[]


for i in range(1,s):
    l.append(abs(k[i]-k[i-1]))
print(min(l))    
