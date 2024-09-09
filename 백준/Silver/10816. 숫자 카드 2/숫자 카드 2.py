from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
req = list(map(int, input().split()))

dic = defaultdict(int)
for num in nums:
    if dic[num] > 0:
        dic[num] += 1
    else:
        dic[num] = 1

ans = []
for x in req:
    ans.append(dic[x])

print(*ans)