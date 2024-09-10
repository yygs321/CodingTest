n,m=map(int,input().split())
trees=list(map(int,input().split()))

l=1
r=max(trees)
result=0

while l<=r:
    mid= (l+r)//2
    cnt=0

    for tree in trees:
        if tree>=mid:
            cnt+=tree-mid
    
    if cnt>=m:
        l=mid+1
        result=max(result,mid)
    else:
        r=mid-1

print(result)