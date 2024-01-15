n = int(input())
lst = [[0]]+[list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(i)] for i in range(n+1)]

dp[1] = lst[1]
for idx in range(2, len(lst)):
    for i in range(idx):
        if i == 0:
            dp[idx][0] = dp[idx-1][0]+lst[idx][0]
            continue
        if i == idx-1:
            dp[idx][-1] = dp[idx-1][-1]+lst[idx][-1]
            continue
        dp[idx][i] = max(dp[idx-1][i-1], dp[idx-1][i])+lst[idx][i]

print(max(dp[n]))