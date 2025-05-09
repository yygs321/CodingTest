from collections import deque
n,k=map(int,input().split())
dp=[float('inf') for _ in range(100001)]

def bfs(cur):
    queue=deque([cur])
    dp[cur]=0

    while queue:
        cur=queue.popleft()

        if cur + 1 <= 100000 and dp[cur + 1] > dp[cur] + 1:
            dp[cur + 1] = dp[cur] + 1
            queue.append(cur + 1)
        if cur-1>=0 and dp[cur-1]>dp[cur]+1:
            dp[cur-1]=dp[cur]+1
            queue.append(cur-1)
        if cur * 2 <= 100000 and dp[cur * 2] > dp[cur]:
            dp[cur * 2] = dp[cur]
            queue.append(cur * 2)

bfs(n)
print(dp[k])