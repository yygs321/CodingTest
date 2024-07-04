def func(x, y, cnt):
    global ans
    if y >= 10:
        ans = min(ans, cnt)
        return

    if x >= 10:
        func(0, y+1, cnt)
        return

    if graph[x][y] == 1:
        for k in range(5):
            if paper[k] == 5:
                continue
            if x + k >= 10 or y + k >= 10:
                continue

            flag = 0
            for i in range(x, x + k + 1):
                for j in range(y, y + k + 1):
                    if graph[i][j] == 0:
                        flag = 1
                        break
                if flag:
                    break

            else:
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        graph[i][j] = 0

                paper[k] += 1
                func(x + k + 1, y, cnt + 1)
                paper[k] -= 1

                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        graph[i][j] = 1
    else:
        func(x + 1, y, cnt)


graph = [list(map(int, input().split())) for _ in range(10)]
paper = [0 for _ in range(5)]
ans = float('inf')

func(0, 0, 0)
if ans != float('inf'):
    print(ans) 
else:
    print(-1)