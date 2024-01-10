# 돈을 최대한 많이 지불해서 카드 N개 구매
n = int(input())
card = [0]+list(map(int, input().split()))
dp = [0]*(n+1)

for i in range(1, n+1):
    dp[i] = max(dp[i], card[i])
    for j in range(1, i):
        if i % j == 0:
            dp[i] = max(dp[i], dp[j]*(i//j))
        dp[i] = max(dp[i], dp[j]+dp[i-j])

print(dp[n])