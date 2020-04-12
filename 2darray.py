l=[]
l3=[]
for i in range(6):
    l.append(input().rstrip().split(" "))
   
for i in range(1,5):
    for j in range(1,5):
        if(int(l[i][j])>=0):
           k=(list(l[i][j])+(l[i-1][j-1:j+2])+l[i+1][j-1:j+2])
           k2=sum(list(map(int,k)))
        else:
            k=(list(l[i][j])+(l[i-1][j-1:j+2])+l[i+1][j-1:j+2])
            k=k[1:]
            k5=(list(map(int,k)))
            k2=sum(k5)-(2*k5[0])
        

        
        l3.append(k2)
        
print(max(l3))
