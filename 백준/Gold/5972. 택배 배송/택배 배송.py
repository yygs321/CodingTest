#가중치 있는 최단거리: 다익스트라
import heapq
from collections import defaultdict

n,m=map(int,input().split())
distance=[int(1e9) for _ in range(n+1)]
queue=[]
graph=defaultdict(list)

for _ in range(m):
    x,y,v=map(int,input().split())
    graph[x].append((v,y))
    graph[y].append((v,x))

distance[1]=0
heapq.heappush(queue,(0,1))
def dijkstra():
    while queue:
        dist, start=heapq.heappop(queue)
        if distance[start]<dist: continue

        for next_dist, next_node in graph[start]:
            if distance[next_node]>dist+next_dist:
                distance[next_node]= dist+next_dist
                heapq.heappush(queue,(dist+next_dist, next_node))

dijkstra()

print(distance[n])
