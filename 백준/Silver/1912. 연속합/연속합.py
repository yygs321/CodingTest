n=int(input())
nums=list(map(int,input().split()))
tmp=-float('inf')
ans=-float('inf')

for num in nums:
    if tmp<0:
        tmp=max(tmp,num)
        ans=max(ans,tmp)
        continue

    tmp+=num
    ans=max(ans,tmp)

print(ans)