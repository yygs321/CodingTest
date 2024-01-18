T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    dp = [[i for i in range(n+1)] for _ in range(k+1)]
    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = sum(dp[i-1][1:j+1])

    print(dp[k][n])