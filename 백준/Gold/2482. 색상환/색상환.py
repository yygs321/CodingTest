mod = 1000000003

n = int(input())
k = int(input())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1  # 0개를 고른 경우는 1개
    dp[i][1] = i  # i개 중 1개를 고르는것: i개

for i in range(2,n+1):
    for j in range(2, k+1):
        if i == n:
            dp[i][j] = (dp[i-3][j-1]+dp[i-1][j]) % mod
        else:
            dp[i][j] = (dp[i-2][j-1] + dp[i-1][j]) % mod


print(dp[n][k])