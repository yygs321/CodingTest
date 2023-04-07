from itertools import combinations

n,m=map(int,input().split())
lst=list(combinations(range(1,n+1),m))
for l in lst:
    print(*l)