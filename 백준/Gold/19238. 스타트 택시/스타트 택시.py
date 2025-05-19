from collections import deque
import heapq

n, m, oil = map(int, input().split())
graph = [[0 for _ in range(n+1)]]+[[0] +list(map(int, input().split())) for _ in range(n)]

taxi_i, taxi_j = map(int, input().split())
customers = [list(map(int, input().split())) for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def distance(i, j):
    queue = deque([(i, j)])
    visited[i][j] = 0
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

            if nx <= 0 or ny <= 0 or nx > n or ny > n:
                continue
            if graph[nx][ny] == 1:
                continue
            if visited[nx][ny] <= visited[x][y]+1:
                continue
            visited[nx][ny] = visited[x][y]+1
            queue.append((nx, ny))


ti, tj = taxi_i, taxi_j
while customers:
    visited = [[float('inf')]*(n+1) for _ in range(n+1)]
    distance(ti, tj)
    hq = []
    for idx, customer in enumerate(customers):
        si, sj, ei, ej = customer
        heapq.heappush(hq, (visited[si][sj], si, sj, ei, ej, idx))

    cur_d, cur_si, cur_sj, cur_ei, cur_ej, cur_idx = heapq.heappop(hq)

    visited = [[float('inf')]*(n+1) for _ in range(n+1)]
    distance(cur_si, cur_sj)
    nxt_d = visited[cur_ei][cur_ej]

    if oil < cur_d+nxt_d:
        oil = -1
        break
    else:
        oil -= (cur_d+nxt_d)
        oil += 2*nxt_d

    customers.pop(cur_idx)
    ti, tj = cur_ei, cur_ej

print(oil)
