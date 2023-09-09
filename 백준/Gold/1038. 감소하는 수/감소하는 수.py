from itertools import combinations

n = int(input())

result = []
for i in range(1, 11):  # 1~10자리수
    for j in combinations(range(10), i):
        tmp = ''.join(reversed(list(map(str, j))))
        result.append(int(tmp))

result.sort()
if len(result) <= n:
    print(-1)
else:
    print(result[n])