n = int(input())
dp = [[0, 0] for _ in range(91)]
dp[1] = [0, 1]
dp[2] = [1, 0]
for i in range(3, n+1):
    # 0의 개수
    dp[i][0] = sum(dp[i-1])
    dp[i][1] = dp[i-1][0]

print(sum(dp[n]))