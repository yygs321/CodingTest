n = int(input())
lst = list(map(int, input().split()))
lst.sort()
tmp = 0
answer = 0
for i in lst:
    tmp += i
    answer += tmp

print(answer)