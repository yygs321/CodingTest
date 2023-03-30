import math
test=int(input())
for tc in range(test):
    n,m=map(int,input().split())
    print(math.comb(m,n))