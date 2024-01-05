n = int(input())
grapes = [0]+[int(input()) for _ in range(n)]
if n < 3:
    print(sum(grapes))
    exit()
dp = [0 for _ in range(n+1)]
dp[1] = grapes[1]
dp[2] = sum(grapes[1:3])
for i in range(3, n+1):
    dp[i] = max(dp[i-2]+grapes[i], dp[i-3]+grapes[i-1]+grapes[i], dp[i-1])

print(dp[n])