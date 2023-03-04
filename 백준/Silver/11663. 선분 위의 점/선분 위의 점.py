import sys
input=sys.stdin.readline

n,m=map(int, input().split())
lst=list(map(int,input().split()))
lst.sort()

def binary_search(v, dir):
    left, right = 0, n-1

    while left <= right:
        mid = (left+right)//2

        if v < lst[mid]:
            right = mid-1
        elif v > lst[mid]:
            left = mid+1
        else:
            return mid

    if dir == 0:
        return left
    else:
        return right


for _ in range(m):
    s, e = map(int, input().split())
    l= binary_search(s, 0)
    r= binary_search(e, 1)
    print(r-l+1)