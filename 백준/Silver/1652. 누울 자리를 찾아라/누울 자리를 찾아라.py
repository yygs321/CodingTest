from collections import deque

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
dx = [0, 1]
dy = [1, 0]
answer = [0, 0]


def bfs(dir, i, j):
    global answer
    visited[i][j] = True
    queue = deque([(i, j)])
    cnt = 1

    while queue:
        x, y = queue.popleft()

        nx = x+dx[dir]
        ny = y+dy[dir]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            break
        if visited[nx][ny]:
            break
        if graph[nx][ny] == "X":
            break
        visited[nx][ny] = True
        cnt += 1
        queue.append((nx, ny))

    if cnt >= 2:
        answer[dir] += 1
        return


for dir in range(2):
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            if graph[i][j] == "X":
                continue
            bfs(dir, i, j)

print(*answer)
