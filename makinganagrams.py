from collections import *    
a = Counter(input())
b = Counter(input())
c = a - b
d = b - a
e = c + d
print (len(list(e.elements())))
