from collections import deque

n=int(input())
graph=[]
for _ in range(n):
  graph.append(list(map(int,input().split())))

result=[[0 for _ in range(n)] for _ in range(n)]

queue=deque()

def dfs(i,j):
    result[i][j]=1
    queue.append(j)
  
    while queue:
        q= queue.popleft()
        for idx,gp in enumerate(graph[q]):
            if gp==1 and result[i][idx]==0:
                result[i][idx]=1
                queue.append(idx)
  
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            dfs(i,j)

for i in range(n):
    for j in range(n):
        print(result[i][j], end=" ")
    print()