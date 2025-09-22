n = int(input())
dp = [0 for _ in range(max(6, n+1))]
dp[3] = 1
dp[5] = 1
for i in range(6, n+1):
    if dp[i-3] == 0 and dp[i-5] == 0:
        continue
    if dp[i-3] != 0 and dp[i-5] != 0:
        dp[i] = min(dp[i-3], dp[i-5])+1
        continue
    if dp[i-3] == 0:
        dp[i] = dp[i-5]+1
    elif dp[i-5] == 0:
        dp[i] = dp[i-3]+1

print(dp[n] if dp[n] != 0 else -1)
