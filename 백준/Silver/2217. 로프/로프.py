n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

num.sort(reverse=True)
answer = 0
for i in range(n, 0, -1):
    answer = max(answer, num[i-1]*i)

print(answer)