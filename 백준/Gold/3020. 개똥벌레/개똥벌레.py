n, h = map(int, input().split())
lst = [0 for _ in range(h+2)]
for i in range(n):
    x = int(input())
    if i % 2 == 0:  # 석순
        lst[1] += 1
        lst[x+1] -= 1
    else:  # 종유석
        lst[h-x+1] += 1
        lst[h+1] -= 1

for i in range(1, h+1):
    lst[i] += lst[i-1]

min_value = min(lst[1:-1])
min_count = lst[1:-1].count(min_value)
print(min_value, min_count)