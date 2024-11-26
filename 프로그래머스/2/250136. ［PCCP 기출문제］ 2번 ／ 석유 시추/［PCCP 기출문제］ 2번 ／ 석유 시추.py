from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    oil = [[-1 for _ in range(m)] for _ in range(n)]
    oil_num = [[-1 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    current_num = 0

    def bfs(i, j, num):
        queue = deque()
        queue.append((i, j))
        visited[i][j] = True
        tmp = 0
        area = []

        while queue:
            x, y = queue.popleft()
            tmp += 1
            area.append((x, y))

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if visited[nx][ny]:
                    continue
                if land[nx][ny] == 0:
                    continue

                visited[nx][ny] = True
                queue.append((nx, ny))

        for x, y in area:
            oil[x][y] = tmp
            oil_num[x][y] = num

    for i in range(n):
        for j in range(m):
            if land[i][j] == 0:
                continue
            if oil[i][j] != -1:
                continue
            bfs(i, j, current_num)
            current_num += 1

    answer = []
    for j in range(m):
        tmp = 0
        num_set = set()
        for i in range(n):
            if oil[i][j] == -1:
                continue
            if oil_num[i][j] in num_set:
                continue
            tmp += oil[i][j]
            num_set.add(oil_num[i][j])
        answer.append(tmp)

    return max(answer)
