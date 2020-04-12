from collections import Counter
s=(input())
s1=Counter(input().split(" "))
s2=Counter(input().split(" "))
if(s2-s1==Counter()):
    print("Yes")
else:
    print("No")
    
