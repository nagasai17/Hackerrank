from collections import Counter
def main():
    mod=10**9+7
    N=int(input())
    A=list(map(int,input().split()))
    d=Counter(A)
    ans=0
    for key in d:
        if key!=0:
            ans+=pow(2,d[key]-1)
        else:
            ans+=(pow(2,d[key])-1)
    print(ans%mod)
