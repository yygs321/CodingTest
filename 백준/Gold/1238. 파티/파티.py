#n개의 마을과 학생, 각 마을에 한명씩 산다
#x번 마을 왕복(오고가는 시간 다름))
#m개의 단방향 도로 i번째 길을 지나는데 T(i)만큼의 시간 소비
#오고가는 각각의 최단시간 중 가장 오래 걸린 시간 출력
import heapq

n,m,x=map(int,input().split())
INF=int(1e9)
graph=[[] for _ in range(n+1)]

#간선 가중치가 다른 최단거리
for i in range(m):
    s,e,t=map(int,input().split())
    #받을때부터 (시간, 위치)순으로 값 삽입
    graph[s].append((t,e))

# print(graph)
# [[], [(2, 4), (3, 2), (4, 7)], [(1, 1), (3, 5)], [(1, 2), (4, 4)], [(2, 3)], [], [], []]

def dijkstra(start):
    q=[]
    distance=[INF for _ in range(n+1)] #1~n
    
    heapq.heappush(q, (0,start))
    distance[start]=0
  
    while q:
        time, now=heapq.heappop(q)
    
        for i in graph[now]:
              next_t, next=i
              if distance[next]> time+next_t:
                  distance[next]=time+next_t
                  heapq.heappush(q, (distance[next], next))
      
    return distance #배열로 반환

result=0
#각 학생들의 거리 계산을 위한 for문
for i in range(1,n+1):
    #dijkstra(i) : i번째 마을에서 시작해서 각 마을까지의 최단거리 배열
    #dijkstra(i)[x] : 그 중 x마을까지 가는데 걸린 시간
    go=dijkstra(i)[x] 
    back=dijkstra(x)[i] # x마을에서 i번째로 돌아오기까지의 최단시간
  
    result=max(result, go+back)

print(result)