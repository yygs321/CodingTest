n=int(input())
nums=[int(input()) for _ in range(n)]
dp=[1 for _ in range(n)]
for i in range(n)[::-1]:
    for j in range(i+1,n):
        if nums[j]>nums[i]:
            dp[i]=max(dp[i], dp[j]+1)

print(n-max(dp))