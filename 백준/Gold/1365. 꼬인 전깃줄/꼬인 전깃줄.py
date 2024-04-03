# 가장 긴 증가하는 부분수열
import bisect

n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]]

for num in nums:
    if dp[-1] < num:
        dp.append(num)
    else:
        idx = bisect.bisect_left(dp, num)
        dp[idx] = num

print(n-len(dp))