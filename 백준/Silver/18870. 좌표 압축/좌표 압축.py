n = int(input())
lst = list(map(int, input().split()))
tmp = sorted(set(lst))
result = {}
for i in range(len(tmp)):
    result[tmp[i]] = i

for l in lst:
    print(result[l], end=' ')
