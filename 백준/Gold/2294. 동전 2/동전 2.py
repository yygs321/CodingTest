import sys
sys.setrecursionlimit(10000)

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [-1] * (k + 1)

def dfs(num):
    if num == 0:
        return 0
    if num < 0:
        return float('inf')

    if dp[num] != -1:
        return dp[num]

    tmp = float('inf')
    for coin in coins:
        tmp = min(tmp, dfs(num - coin) + 1)

    dp[num] = tmp
    return dp[num]

answer = dfs(k)
if answer == float('inf'):
    print(-1)
else:
    print(answer)