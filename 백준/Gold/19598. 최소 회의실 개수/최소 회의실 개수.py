import heapq

n = int(input())
lst = []
for i in range(n):
    s, e = map(int, input().split())
    heapq.heappush(lst, [s, e])

cnt = 1
check = []
while lst:
    start, end = heapq.heappop(lst)
    if check and check[0] <= start:
        heapq.heappop(check)
    heapq.heappush(check, end)

print(len(check))