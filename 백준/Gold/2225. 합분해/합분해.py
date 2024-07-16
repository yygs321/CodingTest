INF = 1000000000

n, k = map(int, input().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
dp[0][0] = 1

for i in range(n+1):
    for j in range(1, k+1):
        for l in range(n+1):
            dp[i][j] += (dp[l][j-1])%INF

print((dp[n][k])%INF)