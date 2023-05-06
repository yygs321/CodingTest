from collections import deque

n=int(input())
time=[0]
indegree=[0]*(n+1)
graph=[[] for _ in range(n+1)]

for i in range(1,n+1):
    tmp=list(map(int,input().split()))
    time.append(tmp.pop(0))
    while tmp:
        x=tmp.pop(0)
        if x==-1: break
        graph[x].append(i)
        indegree[i]+=1


result=[0]*(n+1)
queue=deque()
def solve():
    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append(i)
  
    while queue:
        q=queue.popleft()
        result[q]+=time[q]
        for gp in graph[q]:
            result[gp]=max(result[gp],result[q])
            indegree[gp]-=1
  
            if indegree[gp]==0:
                queue.append(gp)

solve()
print(*result[1:], sep="\n")