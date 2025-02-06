from collections import deque
from bisect import bisect_left
def solution(N, road, K):
    answer = 0

    dp=[float('inf') for _ in range(N+1)]
    graph=[[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    def bfs(start):
        queue=deque()
        dp[start]=0
        queue.append(start)
        
        while queue:
            cur=queue.popleft()
            
            for nxt,nxt_d in graph[cur]:
                if dp[nxt]<=dp[cur]+nxt_d:
                    continue
                dp[nxt]=dp[cur]+nxt_d
                queue.append((nxt))
        
    bfs(1)
    for val in dp:
        if val<=K:
            answer+=1
    return answer