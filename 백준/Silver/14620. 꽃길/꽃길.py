from itertools import combinations
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
lst = []


def bfs(x, y):
    count = graph[x][y]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        count += graph[nx][ny]

    lst.append([count, x, y])


for i in range(1, n-1):
    for j in range(1, n-1):
        bfs(i, j)


def check(x, y):
    global flag
    visited[x][y] = 1

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            flag = 1
            return False
        if visited[nx][ny] == 1:
            flag = 1
            return False

        visited[nx][ny] = 1

    return True


result = int(1e9)
for comb in combinations([i for i in range(len(lst))], 3):

    flag = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    tmp = 0
    for flower in comb:
        c, x, y = lst[flower]

        if visited[x][y] == 1:
            flag = 1
            break

        ok = check(x, y)
        if ok == False:
            break
        else:
            tmp += c

    if flag == 0:
        result = min(result, tmp)

print(result)