import heapq

n, m = map(int, input().split())
present = list(map(int, input().split()))
childrens = list(map(int, input().split()))
present = [-x for x in present]
heapq.heapify(present)

answer = 1

for child in childrens:
    if not present:
        answer = 0
        break
    maxV = -heapq.heappop(present)
    if maxV < child:
        answer = 0
        break
    if maxV != child:
        heapq.heappush(present, -(maxV-child))

print(answer)