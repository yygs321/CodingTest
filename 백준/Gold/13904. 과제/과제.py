import heapq
n = int(input())
lst = [[] for _ in range(1001)]
for i in range(n):
    d, w = map(int, input().split())
    lst[d].append(w)

result = []
for i in range(1001):
    for j in lst[i]:
        if len(result) < i:
            heapq.heappush(result, j)
        else:
            minV = heapq.heappop(result)
            heapq.heappush(result, max(minV, j))

print(sum(result))