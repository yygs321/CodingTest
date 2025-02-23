k = int(input())
coins = [2, 5]
dp = [float('inf') for _ in range(100001)]
dp[0]=0
dp[2]=1
dp[5]=1

for i in range(1, k + 1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] != float('inf') else -1)