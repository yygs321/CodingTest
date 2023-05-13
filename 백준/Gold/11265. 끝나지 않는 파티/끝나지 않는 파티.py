import heapq

n,m=map(int,input().split())

graph=[[0]+list(map(int,input().split())) for _ in range(n)]
graph.insert(0,[0 for i in range(n+1)])


def dijk(start):
    heapq.heappush(q, (0, start))
    result[start]=0
    
    while q:
        t,x=heapq.heappop(q)
        if result[x]<t: continue
    
        for i in range(1,n+1):
            if x==i: continue
            tmp=t+graph[x][i]
            #해당 시간 값보다 작아지는 경우만 
            if tmp<result[i]:
                result[i]=tmp
                heapq.heappush(q, (tmp, i))

    answer[start]=result
    check(result)

def check(result):
    global end
    global time
    if result[end]<=time:
        print("Enjoy other party")
    else:
        print("Stay here")
    

answer=[[] for _ in range(n+1)]
for i in range(m):
    #현재위치, 도착위치, 시간
    start, end, time=map(int,input().split())
    q=[]
    result=[int(1e9) for _ in range(n+1)]
    if answer[start] !=[]: #비어있지 않으면 이미 구해져있는 값
        check(answer[start])
    else:
        dijk(start)