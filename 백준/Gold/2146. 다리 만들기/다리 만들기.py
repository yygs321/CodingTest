from collections import deque

def group(i, j):
    global cnt
    lst[i][j] = cnt
    queue.append((i, j))
  
    while queue:
        x, y = queue.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
      
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if graph[nx][ny] == 0: continue
            
            if lst[nx][ny] == 0:
                lst[nx][ny] = cnt
                queue.append((nx, ny))


def bfs(i, j, num):
    visited[i][j] = 0
    queue.append((i, j, num))
    
    while queue:
        x, y, num = queue.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
      
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if graph[nx][ny] == 1: #섬 일때
                to = lst[nx][ny]
                if num != to: #다른 그룹이면
                    check[num][to] = min(check[num][to], visited[x][y])
                continue
      
            if visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny, num))


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

lst = [[0 for _ in range(n)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

#그룹 짓기
cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and lst[i][j] == 0:
            cnt += 1
            group(i, j)


check = [[int(1e9) for _ in range(cnt+1)] for _ in range(cnt+1)]
for i in range(n):
    for j in range(n):
        visited = [[int(1e9) for _ in range(n)] for _ in range(n)]
        if graph[i][j] == 1:
            num = lst[i][j]
            bfs(i, j, num)

result=int(1e9)
for i in range(cnt+1):
    result=min(result, min(check[i]))

print(result)
'''
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0

3
'''