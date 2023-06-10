from collections import deque

A, B = map(int, input().split())
n, m = map(int, input().split())
robots = {}
graph = [[0 for _ in range(B+1)] for _ in range(A+1)]
# 우하좌상 (y,x)
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
directions = ['E', 'S', 'W', 'N']

for k in range(1, n+1):
    i, j, dir = input().split()
    i, j = int(i), int(j)
    dir = directions.index(dir)
    graph[i][j] = k
    robots[k] = (i, j, dir)

flag = 0
answer = "OK"
queue = deque()

for _ in range(m):
    num, command, repeat = input().split()
    num, repeat = int(num), int(repeat)
    queue.append((num, command, repeat))

while queue:
    num, command, repeat = queue.popleft()
    x, y, d = robots[num]

    for i in range(repeat):
        if command == 'L':
            d = (d+3) % 4
        elif command == 'R':
            d = (d+1) % 4
        else:  # F
            nx = x+dx[d]
            ny = y+dy[d]

            if nx <= 0 or nx > A or ny <= 0 or ny > B:
                flag = 1
                answer = f'Robot {num} crashes into the wall'
                break
            elif graph[nx][ny] != 0:
                flag = 1
                answer = f'Robot {num} crashes into robot {graph[nx][ny]}'
                break

            graph[nx][ny] = graph[x][y]
            graph[x][y] = 0
            x, y = nx, ny

        robots[num] = (x, y, d)  # 로봇 데이터도 바꿔주기

    if flag != 0:
        break

print(answer)

'''
3 3
1 9
2 2 W
1 F 1
1 L 1
1 F 1
1 L 1
1 F 2
1 L 5
1 F 2
1 R 3
1 F 2
'''