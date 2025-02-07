import sys
from collections import defaultdict, deque
import heapq
input=sys.stdin.readline

n,m,r=map(int,input().split())
items=[0]+list(map(int,input().split()))
graph=defaultdict(list)
for _ in range(r):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

dp=[0 for _ in range(n+1)]
result=0
def bfs(start):
    global m,result

    queue=[]
    heapq.heappush(queue,(0,start))
    visited=[float('inf')]*(n+1)
    visited[start]=0
    tmp=items[start]
    selected=set()

    while queue:
        cur_d,cur=heapq.heappop(queue)

        for nxt,nxt_d in graph[cur]:
            if cur_d+nxt_d>m:
                continue
            if visited[nxt]>cur_d+nxt_d:
                visited[nxt]=cur_d+nxt_d
                heapq.heappush(queue,(cur_d+nxt_d,nxt))
                if nxt not in selected:
                    selected.add(nxt)
                    tmp+=items[nxt]

    result=max(result,tmp)

for i in range(1,n+1):
    bfs(i)
print(result)