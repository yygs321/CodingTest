from collections import deque

n,k=map(int,input().split())
dx=[2,-1,1]
queue=deque()
distance=[-1 for _ in range(100001)]

def bfs(start):
    global k
    queue.append(start)
    distance[start]=0
  
    while queue:
        q=queue.popleft()
        if q==k:
            print(distance[q])
            break
          
        for i in range(3):
            if 0<i:
                d=q+dx[i]
                if 0<=d<=100000 and distance[d]==-1:
                    distance[d]=distance[q]+1
                    queue.append(d)
            else:
                d=q*dx[i]
                if 0<=d<=100000 and distance[d]==-1:
                    distance[d]=distance[q]
                    queue.append(d)

bfs(n)