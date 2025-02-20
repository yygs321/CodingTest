from collections import defaultdict
import heapq

def solution(n, roads, sources, destination):
    answer = []
    graph=defaultdict(list)
    
    for road in roads:
        s,e=road
        graph[s].append(e)
        graph[e].append(s)
    
    def bfs(start):
        queue=[]
        heapq.heappush(queue,(0,start))
        visited[start]=0
        
        while queue:
            d,cur=heapq.heappop(queue)
            
            for nxt in graph[cur]:
                if visited[nxt]<=d+1:
                    continue
                visited[nxt]=d+1
                heapq.heappush(queue,(d+1,nxt))
        
        return
    
    visited=[float('inf') for _ in range(n+1)]
    bfs(destination)
    for source in sources:
        answer.append(visited[source] if visited[source]!=float('inf') else -1)
    
    return answer