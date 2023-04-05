from collections import deque

def bfs():
    while q1:
        x, y, cnt = q1.popleft()
        visited[x][y]=cnt

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<r and 0<=ny<c:
                if graph[nx][ny] == "X": continue  # 돌이면
                elif visited[nx][ny]==-1 and graph[nx][ny]!="D":
                    visited[nx][ny]=visited[x][y]+1
                    graph[nx][ny]="*"
                    q1.append((nx,ny,cnt+1))


def bfs2(x,y):
    global result
    visited[x][y] = 0

    while q2:
        x, y = q2.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c:
                if graph[nx][ny] == "X": continue
                elif graph[nx][ny]=="D": #비버 굴 도착
                    result=visited[x][y]+1
                    return
                else:
                    if visited[nx][ny] != -1 and visited[nx][ny] <= visited[x][y] + 1:
                        continue
                    visited[nx][ny]=visited[x][y]+1
                    q2.append((nx,ny))


if __name__ == '__main__':
    r,c=map(int,input().split())
    graph=[]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    for i in range(r):
        graph.append(list(input().rstrip()))

    visited=[[-1 for _ in range(c)] for _ in range(r)]
    water=[]

    q1=deque()
    q2=deque()
    for i in range(r):
        for j in range(c):
            if graph[i][j]=="*":
                cnt=0
                q1.append((i,j,cnt))
            elif graph[i][j]=="S":
                cnt2=0
                p=i
                q=j
                q2.append((i,j))


    result=-1
    bfs()
    bfs2(p,q)

    if result==-1:
        print("KAKTUS")
    else:
        print(result)