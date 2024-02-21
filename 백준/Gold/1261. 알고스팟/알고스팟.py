from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

distance = [[-1 for _ in range(m)] for _ in range(n)]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    distance[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if distance[nx][ny] != -1:
                continue
            if graph[nx][ny] == 0:
                distance[nx][ny] = distance[x][y]
                queue.appendleft((nx, ny))
            else:
                distance[nx][ny] = distance[x][y]+1
                queue.append((nx, ny))


bfs(0, 0)
print(distance[n-1][m-1])