from bisect import bisect_left
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
slst = sorted(input().strip() for _ in range(n))   # 정렬 필수
clst = [input().strip() for _ in range(m)]

cnt = 0
for c in clst:
    idx = bisect_left(slst, c)
    
    if idx < n and slst[idx].startswith(c):
        cnt += 1

print(cnt)
