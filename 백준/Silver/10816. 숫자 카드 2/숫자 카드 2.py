from bisect import bisect_left

n=int(input())
nums=list(map(int,input().split()))
m=int(input())
lst=list(map(int,input().split()))

nums.sort()
result=[]
for val in lst:
    cnt=0

    idx1=bisect_left(nums,val)
    idx2=bisect_left(nums,val+1)
    result.append(idx2-idx1)

print(*result)
