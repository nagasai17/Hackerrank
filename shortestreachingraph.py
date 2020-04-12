t = int(input())
from collections import defaultdict
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = defaultdict(list)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph[x].append(y)
        graph[y].append(x)
    s = int(input())
    q = [s]
    visited = set()
    d = [-1] * n
    d[s-1] = 0
    while q:
        x = q.pop(0)
       
        for y in graph[x]:

            if y not in visited:
                d[y-1] = d[x-1] + 6
                q.append(y)
                visited.add(y)
    print(' '.join(str(x) for x in d[:s-1] + d[s:]))
