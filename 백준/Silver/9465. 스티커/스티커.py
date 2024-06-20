T = int(input())
for _ in range(T):
    n = int(input())
    dp = [[0]+list(map(int, input().split())) for _ in range(2)]

    for j in range(2, n+1):
        for i in range(2):
            if i == 0:
                dp[i][j] += max(dp[1][j-1], dp[1][j-2])
            else:
                dp[i][j] += max(dp[0][j-1], dp[0][j-2])

    print(max(dp[0][n], dp[1][n]))