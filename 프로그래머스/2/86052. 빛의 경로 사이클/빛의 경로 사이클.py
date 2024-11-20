from collections import deque
answer = []

def solution(grid):
    # 동남서북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    n = len(grid)
    m = len(grid[0])

    visited = [[[-1] * 4 for _ in range(m)] for _ in range(n)]

    def bfs(x, y, direction):
        steps = 0
        queue = deque([(x, y, direction)])

        visited[x][y][direction] = steps

        while queue:
            cx, cy, cd = queue.popleft()
            steps += 1

            if grid[cx][cy] == 'L':
                cd = (cd + 3) % 4
            elif grid[cx][cy] == 'R':
                cd = (cd + 1) % 4

            nx, ny = (cx + dx[cd]) % n, (cy + dy[cd]) % m

            if visited[nx][ny][cd] != -1:
                answer.append(steps)
                return

            visited[nx][ny][cd] = steps
            queue.append((nx, ny, cd))

    for i in range(n):
        for j in range(m):
            for d in range(4):
                if visited[i][j][d] == -1:
                    bfs(i, j, d)

    return sorted(answer)
