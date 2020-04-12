for _ in range(int(input())):
    input()
    q = [int(x) for x in input().split()]
    bribes = 0
    valid = True
    for i in reversed(range(len(q))):
        v = i + 1
        if q[-1] == v:
            q.pop(-1)
        elif len(q) > 1 and q[-2] == v:
            q.pop(-2)
            bribes += 1
        elif len(q) > 2 and q[-3] == v:
            q.pop(-3)
            bribes += 2
        else:
            valid = False
            break
    if valid:
        print(bribes)
    else:
        print("Too chaotic")
