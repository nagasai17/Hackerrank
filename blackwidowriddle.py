s=int(input())
for i in range(s):
    k=list(map(int,input().split(" ")))
    l=[]
    for j in range(2,len(k),k[0]):
        l.append(k[j:j+k[0]])
    r=0
    c=0
    for j in l:
        if(k[0]-len(set(j))!=0):
            r+=1
    for j in range(0,k[0]):
        l1=list(map(lambda x:x[j],l))
        if(k[0]-len(set(l1))!=0):
            c+=1
    if(c==0 and r==0):
        print("SAFE")
    else:
        print("DANGER"+" "+str(r)+" "+str(c))
    
 
        



