from collections import deque

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
si, se = map(int, input().split())

# / 이면 +1, \ 이면 -1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction = ['U', 'R', 'D', 'L']
answer = 0


def bfs(i, j, d, tmp):
    global n, m, result_dir

    queue = deque([(i, j, d, tmp)])

    while queue:
        x, y, cur_d, cnt = queue.popleft()

        if cnt > n*m*2:
            return 10000000

        nx = x+dx[cur_d]
        ny = y+dy[cur_d]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return cnt+1

        if graph[nx][ny] == ".":
            queue.append((nx, ny, cur_d, cnt+1))
        elif graph[nx][ny] == "/":
            if cur_d % 2 == 0:
                queue.append((nx, ny, (cur_d + 1) % 4, cnt + 1))
            else:
                queue.append((nx, ny, (cur_d - 1) % 4, cnt + 1))
        elif graph[nx][ny] == "\\":
            if cur_d % 2 == 0:
                queue.append((nx, ny, (cur_d - 1) % 4, cnt + 1))
            else:
                queue.append((nx, ny, (cur_d + 1) % 4, cnt + 1))
        elif graph[nx][ny] == "C":
            return cnt + 1

    return 0


result_dir = ''
for i, d in enumerate(direction):
    tmp = bfs(si-1, se-1, i, 0)
    if answer < tmp:
        result_dir = d
        answer = tmp

print(result_dir)
if answer >= 10000000:
    print("Voyager")
else:
    print(answer)
