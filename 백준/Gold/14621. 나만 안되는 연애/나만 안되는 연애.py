import heapq

n, m = map(int, input().split())
gender = list(input().split())
gender.insert(0, "X")
root = [i for i in range(n+1)]


def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        root[y] = x
    else:
        root[x] = y


queue = []
for i in range(m):
    u, v, d = map(int, input().split())
    heapq.heappush(queue, (d, u, v))

answer = 0
while queue:
    d, u, v = heapq.heappop(queue)

    if gender[u] == gender[v]:
        continue
    if find(u) == find(v):
        continue

    union(u, v)
    answer += d

result = 0
for idx, r in enumerate(root):
    if idx == 0:
        continue
    if idx == r:
        if result == 1:
            print(-1)
            break
        result = 1

else:
    print(answer)