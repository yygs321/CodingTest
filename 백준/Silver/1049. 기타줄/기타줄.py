import heapq
import math

n, m = map(int, input().split())
six_set = []
one_set = []

six_cnt = n//6
one_cnt = n % 6
for _ in range(m):
    s, o = map(int, input().split())
    heapq.heappush(six_set, s)
    heapq.heappush(one_set, o)

s = heapq.heappop(six_set)
o = heapq.heappop(one_set)
if s > 6*o:
    print(n*o)
else:
    up_cnt = math.ceil(n/6)
    print(min(six_cnt*s+one_cnt*o, up_cnt*s))