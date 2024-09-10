n,k=map(int,input().split())
pot=[int(input()) for _ in range(n)]

l=0
r=max(pot)
result=0

while l<=r:
    mid= (l+r)//2
    cnt=0

    
    if mid==0:
        l=mid+1
        continue
    
    for p in pot:
        cnt+=p//mid
    
    if cnt>=k:
        l=mid+1
        result=max(result,mid)
    else:
        r=mid-1

print(result)