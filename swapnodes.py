import sys
sys.setrecursionlimit(1500)

def inorder(n, nodes):
    left, right = nodes[n]
    r = []
    if left != -1:
        r.append(inorder(left, nodes))
    r.append(str(n))
    if right != -1:
        r.append(inorder(right, nodes))
    return ' '.join(r)

def swap(k, n, d, nodes):
    if d % k == 0:
        temp = nodes[n][0]
        nodes[n][0] = nodes[n][1]
        nodes[n][1] = temp
    left, right = nodes[n]
    if left != -1:
        swap(k, left, d+1, nodes)
    if right != -1:
        swap(k, right, d+1, nodes)

n = int(input())
nodes = {}
for i in range(n):
    left, right = map(int, input().split())
    nodes[i+1] = [left, right]
t = int(input())
for _ in range(t):
    k = int(input())
    swap(k, 1, 1, nodes)
    print(inorder(1, nodes))
