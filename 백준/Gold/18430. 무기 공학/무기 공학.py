# 부메랑 중심: 강도 2배
def calIdx(i,j):
    return i*c+j


def check(idx, total):
    global result
    #맨마지막인덱스(r*c-1) 까지 끝내고돌아오면
    if idx==r*c:
        result=max(result, total)
        return

    if visited[idx]==True: return

    x=idx//c
    y=idx%c

    e=calIdx(x,y+1)
    w=calIdx(x,y-1)
    s=calIdx(x+1,y)
    n=calIdx(x-1,y)


    #1번 모양이 가능할 경우
    if (0<=y-1 and visited[w]==False) and (x+1<r and visited[s]==False):
        visited[idx]=True
        visited[w] = True
        visited[s] = True
        for i in range(idx+1, r*c+1):
            check(i, (total+graph[x][y]*2+graph[x][y-1]+ graph[x+1][y]))
        visited[idx] = False
        visited[w] = False
        visited[s] = False

    #2번 모양 가능한 경우
    if (y-1>=0 and visited[w]==False) and (x-1>=0 and visited[n]==False):
        visited[idx] = True
        visited[w] = True
        visited[n] = True
        for i in range(idx + 1, r * c + 1):
            check(i, (total + graph[x][y] * 2 + graph[x][y - 1] + graph[x - 1][y]))
        visited[idx] = False
        visited[w] = False
        visited[n] = False

    #3번모양 가능한 경우
    if (x-1>=0 and visited[n]==False) and (y+1<c and visited[e]==False):
        visited[idx] = True
        visited[n] = True
        visited[e] = True
        for i in range(idx + 1, r * c + 1):
            check(i, (total + graph[x][y] * 2 + graph[x-1][y] + graph[x][y+1]))
        visited[idx] = False
        visited[n] = False
        visited[e] = False

    #4번 모양
    if (x+1<r and visited[s]==False) and (y+1<c and visited[e]==False):
        visited[idx] = True
        visited[s] = True
        visited[e] = True
        for i in range(idx + 1, r * c + 1):
            check(i, (total + graph[x][y] * 2 + graph[x+1][y] + graph[x][y+1]))
        visited[idx] = False
        visited[s] = False
        visited[e] = False


r,c=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(r)]
visited=[False for _ in range(r*c)]
result=0

for i in range(r):
    for j in range(c):
        idx=calIdx(i,j)
        check(idx,0)

print(result)