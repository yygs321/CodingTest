from collections import defaultdict, Counter
import heapq

def solution(n, edge):
    answer = 0
    graph=defaultdict(list)
    
    for eg in edge:
        x,y=eg
        graph[x].append(y)
        graph[y].append(x)
    
    hq=[]
    heapq.heappush(hq,(0,1))
    visited=[False for _ in range(n+1)]
    visited[1]=True
    
    result=[]
    while hq:
        d,cur=heapq.heappop(hq)
        result.append(d)
        
        for nxt in graph[cur]:
            if visited[nxt]:
                continue
            heapq.heappush(hq,(d+1,nxt))
            visited[nxt]=True
    
    answer=Counter(result)[max(result)]
    
    return answer