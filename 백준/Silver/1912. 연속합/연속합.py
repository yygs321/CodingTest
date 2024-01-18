n = int(input())
lst = [0]+list(map(int, input().split()))

dp = [lst[i] for i in range(n+1)]
for i in range(1, n+1):
    if dp[i-1]+lst[i] > 0:
        dp[i] = dp[i-1]+lst[i]
    if dp[i-1]+lst[i] < lst[i]:
        dp[i] = lst[i]


print(max(dp[1:]))