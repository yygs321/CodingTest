import heapq

n = int(input())
lst = []
for i in range(n):
    s, e = map(int, input().split())
    heapq.heappush(lst, [s, e])

cnt = 1
lecture = []
while lst:
    start, end = heapq.heappop(lst)
    if lecture and lecture[0] <= start:
        heapq.heappop(lecture)
    heapq.heappush(lecture, end)

print(len(lecture))