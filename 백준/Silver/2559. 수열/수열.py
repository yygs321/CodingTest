from itertools import accumulate
n, k = map(int, input().split())
lst = list(map(int, input().split()))
lst = [0]+list(accumulate(lst))
answer = -float('inf')

for i in range(k, n+1):
    if i-k >= 0:
        answer = max(answer, lst[i]-lst[i-k])


print(answer)