from collections import deque


n, m, k = map(int, input().strip().split())
candy = [0] + list(map(int, input().strip().split()))

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    members = 1
    total = candy[start]

    while queue:
        x = queue.popleft()

        for nxt in graph[x]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)
                members+=1
                total += candy[nxt]

    groups.append((members, total))

groups = []
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)

dp = [[0 for _ in range(k)] for _ in range(len(groups) + 1)]

for i in range(1, len(groups) + 1):
    members, total = groups[i - 1]

    # i 번째 그룹까지만 있다고 생각했을 때, j명 까지의 최대 사탕 갯수
    for j in range(1, k):
        if j < members:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - members] + total)

print(dp[len(groups)][k-1])