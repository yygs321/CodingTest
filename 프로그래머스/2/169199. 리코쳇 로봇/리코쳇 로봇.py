from collections import deque

def solution(board):
    board = [list(b.rstrip()) for b in board]
    n = len(board)
    m = len(board[0])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[False] * m for _ in range(n)]

    queue = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                queue.append((i, j, 0))
                visited[i][j] = True
                break

    while queue:
        i, j, cnt = queue.popleft()

        if board[i][j] == 'G':
            return cnt

        for k in range(4):
            x, y = i, j

            while True:
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    break
                if board[nx][ny] == 'D':
                    break
                x, y = nx, ny

            if visited[x][y]:
                continue
                
            visited[x][y] = True
            queue.append((x, y, cnt + 1))

    return -1
