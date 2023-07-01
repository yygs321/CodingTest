n, k = map(int, input().split())
lst = list(map(int, input().split()))
track_sum = sum(lst)
lst += reversed(lst)

result = 0
i = 0
flag = 0

for ls in lst:
    result += 1
    i += ls
    if i > k:
        flag = 1
        break


if k <= track_sum:
    print(result)
else:
    print((2*n+1)-result)