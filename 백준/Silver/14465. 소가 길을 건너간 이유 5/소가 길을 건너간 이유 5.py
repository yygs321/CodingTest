n,k,b=map(int,input().split())
nums=[1]*(n+1)
for _ in range(b):
    x=int(input())
    nums[x]=0
zero=[0]*(n+1)
for i in range(1,n+1):
    if nums[i]==0:
        zero[i]=zero[i-1]+1
    else:
        zero[i]=zero[i-1]

answer=float('inf')
for i in range(n,k-1,-1):
    answer=min(answer, zero[i]-zero[i-k])

print(answer)