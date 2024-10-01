from copy import deepcopy
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# cctv
dx = [[], [[0], [0], [1], [-1]], [[0, 0], [1, -1]], [[-1, 0], [0, 1], [1, 0],
                                                     [0, -1]], [[0, -1, 0], [-1, 0, 1], [0, 1, 0], [1, 0, -1]], [[0, -1, 0, 1]]]
dy = [[], [[1], [-1], [0], [0]], [[1, -1], [0, 0]], [[0, 1], [1, 0], [0, -1],
                                                     [-1, 0]], [[-1, 0, 1], [0, 1, 0], [1, 0, -1], [0, -1, 0]], [[-1, 0, 1, 0]]]


def dfs(i, j, now_graph, xlst, ylst):
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[i][j] = True

    queue = deque()

    for k in range(len(xlst)):
        queue.append((i, j, k))

    while queue:
        p, q, dir = queue.popleft()

        nx = p+xlst[dir]
        ny = q+ylst[dir]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if visited[nx][ny] == True:
            continue

        if now_graph[nx][ny] in (-1, 1, 2, 3, 4, 5):
            queue.append((nx, ny, dir))
            continue

        if now_graph[nx][ny] == 0:
            now_graph[nx][ny] = -1
            visited[nx][ny] = True
            queue.append((nx, ny, dir))

    return now_graph


def backTracking(i, j, new_graph):
    cctv_num = new_graph[i][j]
    tmp_lst = []

    for xlst, ylst in zip(dx[cctv_num], dy[cctv_num]):
        # 각 방향마다의 이동값 x,y
        tmp_lst.append(dfs(i, j, deepcopy(new_graph), xlst, ylst))

    return tmp_lst


cctv_lst = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            continue
        if graph[i][j] == 6:
            continue
        cctv_lst.append((i, j))

if not cctv_lst:
    cnt = 0
    for i in range(n):
        cnt += graph[i].count(0)
    print(cnt)
    exit()

graph_queue = deque()
graph_queue.append(deepcopy(graph))
for cctv in cctv_lst:
    i, j = cctv
    tmp_lst = []
    while graph_queue:
        gq = graph_queue.popleft()

        tmp_lst += backTracking(i, j, gq)

    for tmp in tmp_lst:
        graph_queue.append(tmp)

ans = float('inf')
for new_graph in graph_queue:
    cnt = 0
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 0:
                cnt += 1

    ans = min(ans, cnt)

print(ans)