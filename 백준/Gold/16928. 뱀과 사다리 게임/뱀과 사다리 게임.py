from collections import deque

n, m = map(int, input().split())
visited = [[float('inf') for j in range(10)] for i in range(10)]

ladder = {}
snake = {}
queue = deque()

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

result = float('inf')
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
        nxt = ladder[value]
        dfs(nxt, count)
    elif value in list(snake.keys()):
        nxt = snake[value]
        dfs(nxt, count)
    else:
        for k in range(1, 7):
            if value + k > 100:
                break
            nxt = value + k
            dfs(nxt, count + 1)

dfs(1,0)
print(result)