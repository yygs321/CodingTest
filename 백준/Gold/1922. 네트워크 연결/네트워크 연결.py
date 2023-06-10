# 모든 컴퓨터를 연결할 최소비용
import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
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
answer = 0
for i in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(queue, (c, a, b))

while queue:
    c, a, b = heapq.heappop(queue)
    if find(a) == find(b):
        continue

    union(a, b)
    answer += c

print(answer)