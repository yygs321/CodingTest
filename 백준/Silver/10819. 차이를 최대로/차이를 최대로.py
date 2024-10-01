from itertools import permutations

n = int(input())
nums = sorted(list(map(int, input().split())))

ans = 0
for perm in (permutations(nums, n)):
    tmp = 0
    for i in range(1, n):
        tmp += abs(perm[i-1]-perm[i])

    ans = max(ans, tmp)

print(ans)