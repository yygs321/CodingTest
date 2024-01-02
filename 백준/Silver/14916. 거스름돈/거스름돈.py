n = int(input())

cnt = int(1e9)
if n % 5 == 0:
    cnt = n//5

max_two = n//2
for i in range(max_two, 0, -1):
    tmp = n - (2*i)
    if tmp % 5 != 0:
        continue
    cnt = min(cnt, i+tmp//5)

if cnt == int(1e9):
    cnt = -1
print(cnt)