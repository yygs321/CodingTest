n = int(input())
cur_start, cur_end = -int(1e9), -int(1e9)
result = 0

lst = []
for i in range(n):
    s, e = map(int, input().split())
    lst.append((s, e))

lst.sort()
for s, e in lst:
    if cur_end < s:
        result += (cur_end-cur_start)
        cur_start = s
    cur_end = max(cur_end, e)

# 마지막 길이 더해주기
result += cur_end-cur_start
print(result)