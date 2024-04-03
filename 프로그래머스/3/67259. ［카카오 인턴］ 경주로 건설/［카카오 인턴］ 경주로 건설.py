from collections import deque

#동서남북
dx=[0,0,1,-1] 
dy=[1,-1,0,0]
def solution(board):
    n=len(board)
    def bfs(board, dir):
        graph=[[int(1e9) for _ in range(n)] for _ in range(n)]
        graph[0][0]=0
        queue=deque()
        queue.append((0,0,0,dir))
        
        while queue:
            x,y,cost,d=queue.popleft()

            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if board[nx][ny] == 1:
                    continue
                    
                if k==d: #직선방향
                    nc=cost+100
                else:
                    nc=cost+600
                
                if nc<graph[nx][ny]:
                    graph[nx][ny]=nc
                    queue.append((nx,ny,nc,k))
                    
        return graph[n-1][n-1]
    
    #동쪽, 남쪽 방향 중 작은 것
    answer = min(bfs(board, 0), bfs(board,2))
    return answer