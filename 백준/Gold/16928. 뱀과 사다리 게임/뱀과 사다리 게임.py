#도착한 칸: 사다리- 더 큰 수
#도착한 칸 : 뱀 - 작은 수
#주사위 굴리는 횟수 최솟값
from collections import deque

INF=int(1e9)

n, m = map(int, input().split())
#이동하는 칸의 번호를 넣는다
visited = [[INF for j in range(10)] for i in range(10)]

ladder = {}
snake = {}
queue = deque()

#사다리
for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

#뱀
for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

result = INF
def dfs(value, count):
    global result
  
    if value == 100:
        result = min(result, count)
        return
      
    i = value // 10
    j = value % 10 - 1
    if visited[i][j]>count:
        visited[i][j] = count
    else:
        return
  
    if value in list(ladder.keys()):
        next = ladder[value]
        dfs(next, count) #주사위굴리는게 아니니까 count 그대로
    elif value in list(snake.keys()):
        next = snake[value]
        dfs(next, count)
    else:
        for k in range(1, 7):
            if value + k > 100:
                break
            next = value + k
            dfs(next, count + 1)

dfs(1,0)
print(result)