import heapq

n = int(input())
queue = []
dasom = 0
start = 0

if n == 1:
    print(0)
    exit()

for i in range(n):
    x = int(input())
    if i == 0:
        dasom = x
        start = x
        continue  # 다솜이건 힙에 안넣음

    heapq.heappush(queue, -x)

while queue:
    q = -heapq.heappop(queue)
    if q < dasom:
        print(abs(dasom-start))
        break

    q -= 1
    dasom += 1
    heapq.heappush(queue, -q)
