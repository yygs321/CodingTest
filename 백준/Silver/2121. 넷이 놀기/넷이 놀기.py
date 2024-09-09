n = int(input())
w, h = map(int, input().split())
dots = set()
for _ in range(n):
    x, y = map(int, input().split())
    dots.add((x, y))

cnt = 0
for x, y in dots:
    if ((x+w, y) in dots) and ((x, y+h) in dots) and ((x+w, y+h) in dots):
        cnt += 1

print(cnt)