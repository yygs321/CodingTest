from collections import deque

r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check():
    queue = deque()
    visited = [[0 for _ in range(c)] for _ in range(r)]

    visited[0][0] = 1
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if visited[nx][ny] == 1:
                continue

            visited[nx][ny] = 1
            if graph[nx][ny] == 1:
                # 치즈 녹이고 queue에 추가안함(바깥쪽 치즈만 고려하면되므로)
                graph[nx][ny] += 1
            else:
                queue.append((nx, ny))

    count()


def count():
    global cnt
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 1:
                cnt += 1


time = 0
cnt = 0
count()  # 가장 처음 개수
answer = []
answer.append(cnt)


while True:
    cnt = 0
    time += 1
    check()

    if cnt == 0:
        print(time)
        print(answer[-1])
        break

    answer.append(cnt)
