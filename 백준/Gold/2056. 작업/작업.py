from collections import deque

def solve():
    global n
    global result
    queue = deque()

    #전입차수가 0인게 1만 있는건 아니므로 전체 돌면서 queue에 넣어주기
    for i in range(1,n+1):
        if inlst[i]==0:
            visited[i]=time[i]
            queue.append(i)

    while queue:
        k= queue.popleft()

        for gp in graph[k]:
            if inlst[gp]!=0:
                inlst[gp] -= 1
            #전입값들을 현재값에 넣으면서 계속 갱신
            visited[gp]=max(visited[gp],visited[k]) 
            if inlst[gp] == 0:
                #위에서 전입값
                visited[gp]+=time[gp]
                queue.append(gp)


n = int(input())
# 진입차수 개수
inlst = [0 for i in range(n + 1)]
time = [0 for i in range(n + 1)]
graph = [[] for i in range(n + 1)]
visited=[0 for i in range(n+1)]

for i in range(1, n + 1):
    # 걸린 시간, 선행작업 개수, 작업 번호
    tmp = list(map(int, input().split()))
    time[i] =  tmp[0]
    inlst[i] =  tmp[1]
    for l in tmp[2:]:
        graph[l].append(i)


solve()

print(max(visited))