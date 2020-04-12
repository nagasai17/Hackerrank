s=input()
h={}
for i in s:
    if(i in h):
        h[i]+=1
    else:
        h[i]=1
k=list((h.values()))
# l=[]
# if(len(set(k))==1):
#     l.append(0)
# elif(len(set(k))==2):
#     kz=k.index(max(k))
#     k[kz]=k[kz]-1
#     if(len(set(k))==1):
#         l.append(0)
#     k[kz]=k[kz]+1
#     km=k.index(min(k))
#     k[km]=k[km]+1
#     if(len(set(k))==1):
#         l.append(0)                
# if(0 in l):
#     print("YES")

# else:
#     print("NO")
c=0
for i in k:
    if(i!=k[0]):
        c=c+1
if(c>1):
    print("NO")
else:
    print("YES")    


