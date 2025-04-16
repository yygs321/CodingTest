from collections import defaultdict

n,d=(map(int,input().split()))

road=defaultdict(list)
for _ in range(n):
    s,e,k=map(int,input().split())

    road[s].append((e,k))

dp=[i for i in range(d+1)]
def dfs(end,total):
    if end>d:
        return
    if dp[end]<total:
        return
    else:
        dp[end]=total

    for nxt in road[end]:
        dfs(nxt[0],total+nxt[1])
    dfs(end+1,total+1)

dfs(0,0)
print(dp[d])

