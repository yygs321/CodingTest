from collections import deque

n=int(input())
a,b=map(int,input().split())
m=int(input())
#부모자식 x,y/  x가 y의 부모
family=[[] for _ in range(n+1)]
for _ in range(m):
    parent, child=map(int,input().split())
    family[parent].append(child)
    family[child].append(parent)

visited=[-1 for _ in range(n+1)]
def bfs(i):
    queue=deque()
    queue.append(i)
    visited[i]=0

    while queue:
        x=queue.popleft()
        
        for child in family[x]:
            if visited[child]!=-1:
                continue
            visited[child]=visited[x]+1
            queue.append(child)

bfs(a)
print(visited[b])