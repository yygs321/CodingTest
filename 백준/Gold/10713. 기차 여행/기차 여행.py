# n: 도시 수, m: 이동 수
n, m = map(int, input().split())
travel = list(map(int, input().split()))
cost = [[0, 0, 0]]
for i in range(n-1):
    cost.append(list(map(int, input().split())))

road = [0 for _ in range(n+1)]
for i in range(m-1):
    start = min(travel[i], travel[i+1])
    end = max(travel[i], travel[i+1])

    road[start] += 1
    road[end] -= 1

prefix_sum = [0 for _ in range(n+1)]
for i in range(1, n+1):
    prefix_sum[i] = road[i]+prefix_sum[i-1]

result = 0
for i in range(1, n):
    x, y, z = cost[i]
    num = prefix_sum[i]
    result += min(x*num, z+y*num)

print(result)