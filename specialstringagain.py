import re
s=int(input())
k=0
s1=list(input())
def triangular_number(n): 
    return (pow(n,2)+n)//2

def substrCount(n, s):
    count = len(s)

    exp1 = r'(([a-z])\2*)(?!\1)(?=[a-z]\1)'
    m = re.finditer(exp1,s)
    count += sum([len(x.group(0)) for x in m])

    exp2 = r'([a-z])\1+'
    m = re.finditer(exp2,s)
    count += sum([triangular_number(len(x.group(0))-1) for x in m])

    return count
print(substrCount(s, "".join(s1)))  
     
