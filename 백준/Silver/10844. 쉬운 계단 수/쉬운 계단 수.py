INF = 1000000000

n = int(input())

dp = [[0 for _ in range(10)] for _ in range(101)]

dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, 101):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1] % INF
            continue
        if j == 9:
            dp[i][j] = dp[i-1][8] % INF
            continue
        dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1]) % INF

print(sum(dp[n]) % INF)
