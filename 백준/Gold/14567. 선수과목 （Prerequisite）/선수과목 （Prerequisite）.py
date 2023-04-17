# 앞선 과목 먼저 이수해야 해당과목 이수 가능
# a,b : a과목이 b의 선수과목 a->b
from collections import deque

def solve():
    queue=deque()
    
    for i in range(1,n+1):
        if inlst[i]==0:
            queue.append((i,1))
  
    while queue:
        x,cnt=queue.popleft()
        result[x-1]=cnt
        
        for gp in graph[x]:
            #진입차수 하나씩 줄여주기
            inlst[gp]-=1
            if inlst[gp]==0:
                queue.append((gp,cnt+1))

n,m=map(int,input().split())
#진입차수
inlst=[0 for ㅑ in range(n+1)]
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    #진입차수 1 증가
    inlst[b]+=1
  
result=[[0] for _ in range(n)]
solve()
print(*result)