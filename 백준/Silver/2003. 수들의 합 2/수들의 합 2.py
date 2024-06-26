n, m = map(int, input().split())
lst = list(map(int, input().split()))

for i in range(1, n):
    lst[i] += lst[i-1]

result = 0
for i in range(n):
    for j in range(i):
        if lst[i]-lst[j] == m:
            result += 1
    if lst[i] == m:
        result += 1

print(result)
