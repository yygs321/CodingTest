n = int(input())
time = [300, 60, 10]

cnt = [0, 0, 0]
for idx, t in enumerate(time):
    if n//t == 0:
        continue
    cnt[idx] += n//t
    n %= t

if n != 0:
    print(-1)
else:
    print(*cnt)