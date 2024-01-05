def change(x, y):
    for i in range(3):
        for j in range(3):
            if graphA[x+i][y+j] == 0:
                graphA[x+i][y+j] = 1
            elif graphA[x+i][y+j] == 1:
                graphA[x+i][y+j] = 0
    return


n, m = map(int, input().split())
graphA = []
graphB = []
for i in range(n):
    graphA.append(list(map(int, input().rstrip())))

for i in range(n):
    graphB.append(list(map(int, input().rstrip())))

cnt = 0
for i in range(1, n-1):
    for j in range(1, m-1):
        if graphA[i-1][j-1] != graphB[i-1][j-1]:
            cnt += 1
            change(i-1, j-1)

for a, b in zip(graphA, graphB):
    if a != b:
        print(-1)
        exit()

print(cnt)