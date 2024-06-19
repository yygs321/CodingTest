from collections import deque

n = int(input())
graph = [input().rstrip() for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j, m):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    q = graph[i][j]

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == True:
                continue
            if graph[nx][ny] != q:
                if m == 0:
                    continue
                else:
                    if not ((q == 'G' and graph[nx][ny] == 'R') or (q == 'R' and graph[nx][ny] == 'G')):
                        continue
            visited[nx][ny] = True
            queue.append((nx, ny))

    return 1


result = [0, 0]
for m in range(2):
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == True:
                continue
            result[m] += bfs(i, j, m)

print(*result)