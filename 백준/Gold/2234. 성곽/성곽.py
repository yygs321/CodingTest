# 1 0001 서
# 2 0010 북
# 4 0100 동
# 8 1000 남
from collections import deque, defaultdict

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
# 칸값을 2진수 리스트로 담고 4방향 중 0인 방향만 bfs돌리기
direction = [1, 2, 4, 8]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(i, j, r):
    queue = deque()
    visited[i][j] = r
    queue.append((i, j))

    cnt = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            # 벽이면 패쓰
            if graph[x][y] & direction[k] > 0:
                continue
            nx = x+dx[k]
            ny = y+dy[k]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] != 0:
                continue
            cnt += 1
            visited[nx][ny] = r
            queue.append((nx, ny))

    return cnt


visited = [[0 for _ in range(n)] for _ in range(m)]
room = defaultdict(int)
r = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] != 0:
            continue
        r += 1

        room[r] = bfs(i, j, r)


result = 0
for i in range(m):
    for j in range(n):
        for k in range(4):
            # 벽일때 체크
            if graph[i][j] & direction[k] == 0:
                continue
            nx = i+dx[k]
            ny = j+dy[k]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            # 같은방이면 패쓰
            if visited[i][j] == visited[nx][ny]:
                continue
            result = max(result, room[visited[i][j]] + room[visited[nx][ny]])


print(len(list(room.keys())))
print(max(list(room.values())))
print(result)