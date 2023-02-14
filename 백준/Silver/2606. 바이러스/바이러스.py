from collections import deque

com=int(input())
n=int(input())
graph=[[]*(com+1) for _ in range(com+1)]


def bfs(start):
    global visited # global 정의할때 
    visited=[] # 초기화랑 따로해야함
    queue=deque([start])
    visited.append(start)
    while queue:
        x=queue.popleft()
        for i in graph[x]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

for i in range(n):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
        
print(len(visited)-1) #첫 시작 1번컴퓨터 제외