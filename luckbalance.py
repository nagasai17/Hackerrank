#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    c=sorted(contests,key=(lambda x:x[1]))
    c1=list(filter(lambda x:x[1]>0,c))
    c0=list(filter(lambda x:x[1]==0,c))
    c1=list(map(lambda x:x[0],c1))
    c0=sum(list(map(lambda x:x[0],c0)))
    c1.sort()
    c1.reverse()
    c3=sum(c1[:k])-sum(c1[k:])
    return c3+c0
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
