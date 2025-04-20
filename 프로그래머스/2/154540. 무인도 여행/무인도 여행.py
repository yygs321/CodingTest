from collections import deque

def solution(maps):
    answer = []
    graph = []
    for map in maps:
        graph.append(list(map))
    
    n = len(graph)
    m = len(graph[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(i, j):
        tmp = int(graph[i][j])
        q = deque()
        q.append((i, j))
        visited[i][j] = True
        
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if visited[nx][ny]:
                    continue
                if graph[nx][ny] == 'X':
                    continue
                
                visited[nx][ny] = True
                tmp += int(graph[nx][ny])
                q.append((nx, ny))
        
        return tmp
        
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'X':
                continue
            if visited[i][j]:
                continue
            visited[i][j] = True
            answer.append(bfs(i, j))
    
    return sorted(answer) if answer else [-1]
