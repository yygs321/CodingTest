n = int(input())
lst = list(map(int, input().split()))
l = 0
r = len(lst)-1
result = float('inf')
m = 0
while l < r:
    if result > abs(lst[r]+lst[l]):
        result = abs(lst[r]+lst[l])
        if lst[r]+lst[l] == abs(lst[r]+lst[l]):
            m = 1
        else:
            m = -1

    if lst[l]+lst[r] > 0:
        r -= 1
    elif lst[l]+lst[r] < 0:
        l += 1
    else:
        break

print(m*result)