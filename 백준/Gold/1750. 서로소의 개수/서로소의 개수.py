import math
n = int(input())

# 각 인덱스는 가능한 최대공약수
S = [int(input()) for _ in range(n)]
dp = [0 for _ in range(max(S)+1)]

for i in range(n):
    for j in range(1, len(dp)):
        if dp[j] > 0:
            dp[math.gcd(j, S[i])] += dp[j]
    dp[S[i]] += 1
print(dp[1] % 10000003)