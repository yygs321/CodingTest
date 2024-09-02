n=int(input())
nums=sorted(list(map(int,input().split())))
x=int(input())
l=0
r=n-1
cnt=0
while l<r:
    tmp=nums[l]+nums[r]
    if tmp<x:
        l+=1
    elif tmp==x:
        cnt+=1
        l+=1
        r-=1
    else:
        r-=1

print(cnt)