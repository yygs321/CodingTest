#D 킬로미터 길이 고속도로
#운전야하는 거리의 최솟값 => 마지막까지의 거리

#지름길 개수 n, 고속도로 길이 d
import heapq

n,d=map(int,input().split())

INF=1e9
distance=[INF]*(d+1)
graph=[[] for _ in range(d+1)]

for i in range(d):
    graph[i].append((i+1, 1))  

for i in range(n):
    #시작위치, 도착위치, 지름길 길이
    #거리 최솟값 -> 다익스트라 알고리즘
    s,e,l=map(int,input().split())
    #끝나는 지점이 고속도로 길이보다 이상이면 패스
    if e>d: 
      continue
    graph[s].append((e,l))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
  
    while q:
        dist, now= heapq.heappop(q)
  
        if dist>distance[now]:
            continue
    
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]= cost
                #제일 작은 값
                heapq.heappush(q, (cost,i[0]))

dijkstra(0)
print(distance[d])