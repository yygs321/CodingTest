n = int(input())
dp = [0 for _ in range(n+1)]
if n <= 2:
    print(n)
    exit()
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n]%10007)