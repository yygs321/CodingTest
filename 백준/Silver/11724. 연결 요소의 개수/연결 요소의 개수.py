from collections import deque


def bfs(i):
    queue = deque()
    queue.append(i)
    visited[i] = True

    while queue:
        x = queue.popleft()
        for q in graph[x]:
            if visited[q]:
                continue
            visited[q] = True
            queue.append(q)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(n+1)]
cnt = 0
for i in range(1, n+1):
    if visited[i]:
        continue
    cnt += 1
    bfs(i)

print(cnt)