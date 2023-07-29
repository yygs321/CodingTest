import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

def dfs(root_node):
    result[root_node] = 1
    for sub in tree[root_node]:
        if not result[sub]:
            dfs(sub)
            result[root_node] += result[sub]


# 정점 수, 루트 번호, 쿼리 수
n, r, q = map(int, input().split())
tree = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]
for i in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(r)

for i in range(q):
    u = int(input())
    print(result[u])