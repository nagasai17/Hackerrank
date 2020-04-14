s=int(input())
for i in range(s):
    n,p=map(int,input().split(" "))
    if(n*(n+1)//2 <=p):
        k=[str(i) for i in range(1,n+1)]
        z1=int(k[0])
        z=p-(n*(n+1)//2)
        k[0]=str(z+z1)
        print(" ".join(k))
    else:
        k=[[]for i in range(0,n)]
        c=0
        i1=0
        j=0
        while(c<p):
            k[j].append(1)
            c+=1
            j=j+1
            if(j==n):
                j=i1+1
                i1=i1+1
        l=list(map(lambda x:str(len(x)),k))
        print(" ".join(l))
                
                
                
            
