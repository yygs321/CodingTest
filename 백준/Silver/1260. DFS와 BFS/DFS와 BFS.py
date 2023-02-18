from collections import deque
from collections import defaultdict
#N: 정점개수
#M: 간선 개수
#V: 탐색 시작정점
N,M,V= map(int,input().split())
stack=deque()
queue=deque()
lst=defaultdict(list)

for i in range(M):
    x,y=map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)


def dfs(stack, V, visited):
    stack.append(V)
    while stack:
        x=stack.pop()

        if x not in visited:
            print(x, end=" ")
            visited.append(x)
            for ls in sorted(lst[x]): #정점 작은것부터 방문
                dfs(stack, ls, visited)
            

def bfs(queue, V, visited):
    queue.append(V)
    while queue:
        y= queue.popleft()

        if y not in visited:
            print(y, end=" ")
            visited.append(y)
            for ls in sorted(lst[y]):
                queue.append(ls)
            
visited=[]
dfs(stack, V, visited)
print()
visited=[]
bfs(queue,V, visited)