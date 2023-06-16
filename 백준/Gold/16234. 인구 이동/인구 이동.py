# 두 나라 인구차이: L이상 R 이하 -> 국경선 연다
# 하루동안 연합
# 각 칸: 연합 인구수 // 연합 이루는 칸의 수
from collections import deque


def dfs(x, y):
    global total
    global cnt

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny] == True:
            continue
        if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
            queue.append((nx, ny))
            visited[nx][ny] = True
            total += graph[nx][ny]
            cnt += 1
            dfs(nx, ny)

    return


N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]

    flag = 0
    for i in range(N):
        for j in range(N):
            queue = deque()
            total = graph[i][j]
            cnt = 1
            if visited[i][j] == True:
                continue
            visited[i][j] = True
            queue.append((i, j))

            dfs(i, j)

            while queue:
                x, y = queue.popleft()
                if queue:
                    flag = 1  # 1개이상이면 변경
                graph[x][y] = total//cnt

    if flag == 0:
        break

    answer += 1


print(answer)