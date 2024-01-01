n = int(input())
score = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

# 나이순 모여있는애들끼리 한 조
for i in range(1, n+1):
    max_val = 0
    min_val = int(1e9)
    for j in range(i-1, -1, -1):
        max_val = max(max_val, score[j])
        min_val = min(min_val, score[j])
        dp[i] = max(dp[i], max_val-min_val+dp[j])

print(dp[n])
