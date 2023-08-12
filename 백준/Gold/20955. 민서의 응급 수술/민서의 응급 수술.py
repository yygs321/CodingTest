n, m = map(int, input().split())
root = [i for i in range(n+1)]


def union(x, y):
    xroot = find(x)
    yroot = find(y)

    if xroot < yroot:
        root[yroot] = xroot
    else:
        root[xroot] = yroot


def find(x):
    if root[x] != x:
        return find(root[x])

    return x


result = 0
for i in range(m):
    u, v = map(int, input().split())

    # union하기 전 동일한 부모: 사이클 -> 끊어줘야함
    if find(u) == find(v):
        result += 1
    union(u, v)

for i in range(1, n):
    if find(i) != find(i+1):
        union(i, i+1)
        result += 1

print(result)