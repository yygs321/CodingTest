# F: 꽃, g: Tmfprl
# 쓰레기는 최대한 적게
# 지나는 횟수 동일 -> 쓰레기 옆을 지나가는것도 최소
# S -> F로 이동
# g: 훨씬 큰 수, g주변 :1  (s,f,g 가 아니먄)


import heapq


def change(x, y):
    # 주변 다 밟은 것보다 더 뒷순위여야 하므로 50x50 다 합친것보다 큰 값으로 설정
    graph[x][y] = 3000
    visited[x][y] = True

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visited[nx][ny] == True:
            continue
        if graph[nx][ny] == 'g' or graph[nx][ny] == 'S' or graph[nx][ny] == 'F':
            continue
        # . 인 g 주변만 1로
        graph[nx][ny] = 1
        visited[nx][ny] = True


def bfs(i, j):
    heapq.heappush(queue, (0, i, j))
    visited[i][j] = True

    while queue:
        v, x, y = heapq.heappop(queue)

        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == True:
                continue
            if graph[nx][ny] == 'F':  # 도착지
                return v

            visited[nx][ny] = True
            if graph[nx][ny] == '.':
                heapq.heappush(queue, (v, nx, ny))
            else:
                heapq.heappush(queue, (v+graph[nx][ny], nx, ny))


n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
startX, startY = 0, 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            startX, startY = i, j
            graph[i][j] = 0
        elif graph[i][j] == 'g':
            change(i, j)


visited = [[False for _ in range(m)] for _ in range(n)]
queue = []
answer = bfs(startX, startY)

print(f'{answer//3000} {answer%3000}')