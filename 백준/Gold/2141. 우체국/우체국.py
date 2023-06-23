import heapq

n = int(input())
total = 0
X = []
for i in range(1, n+1):
    x, a = map(int, input().split())
    X.append([x, a])
    total += a

X.sort(key=lambda x: x[0])
cnt = 0
for i in range(n):
    cnt += X[i][1]
    if cnt >= total/2:
        print(X[i][0])
        break