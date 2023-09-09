from itertools import combinations
from collections import deque

graph = [list(input().rstrip()) for _ in range(5)]
number = [[0 for _ in range(5)] for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0


def bfs(i, j):
    global result
    queue = deque()
    visited = [[False for _ in range(5)] for _ in range(5)]
    cnt = 0
    total = 1

    queue.append((i, j))
    visited[i][j] = True
    if graph[i][j] == 'S':
        cnt += 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if visited[nx][ny] == True:
                continue
            if number[nx][ny] == 0:
                continue

            total += 1
            visited[nx][ny] = True
            if graph[nx][ny] == 'S':
                cnt += 1
            queue.append((nx, ny))

    if total == 7:
        if cnt >= 4:
            result += 1


# 0~24까지 번호를 매김
for comb in combinations(range(25), 7):
    for c in comb:
        number[c//5][c % 5] = 1

    bfs(comb[0]//5, comb[0] % 5)

    # 다음 조합을 위해 0으로 초기화
    for c in comb:
        number[c//5][c % 5] = 0


print(result)