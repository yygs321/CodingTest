import sys
input=sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))
m=int(input())
check=list(map(int,input().split()))
result=[0]*m


# -10 -10 2 3 3 6 7 10 10 10
def bin(start, end, i):
    x=check[i]
    if start>end:
        return

    mid=(start+end)//2
    if lst[mid]==x:
        result[i]=lst[start:end+1].count(x)
        return

    if x>lst[mid]:
        bin(mid+1, end, i)
    else:
        bin(start, mid-1, i)

find={}
lst.sort()
for i,c in enumerate(check):
    if c in find:
        result[i]=find[c]
        continue
    bin(0,n-1,i)
    find[c]=result[i]

print(*result)