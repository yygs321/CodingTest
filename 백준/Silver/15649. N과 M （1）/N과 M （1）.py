from itertools import permutations as p
n,m=map(int,input().split())
num=[i for i in range(1,n+1)]
lst=list(p(num,m))
for ls in lst:
    for l in ls:
        print("%d" %l, end=' ')
    print()