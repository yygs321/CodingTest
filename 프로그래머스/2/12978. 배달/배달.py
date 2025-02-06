from collections import deque
def solution(N, road, K):
    answer = 0

    distance=[float('inf') for _ in range(N+1)]
    graph=[[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    def bfs(start):
        queue=deque()
        distance[start]=0
        queue.append(start)
        
        while queue:
            cur=queue.popleft()
            
            for nxt,nxt_d in graph[cur]:
                if distance[nxt]<=distance[cur]+nxt_d:
                    continue
                distance[nxt]=distance[cur]+nxt_d
                queue.append((nxt))
        
    bfs(1)
    for val in distance:
        if val<=K:
            answer+=1
    return answer