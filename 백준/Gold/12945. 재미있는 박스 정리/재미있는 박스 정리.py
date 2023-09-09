n = int(input())
box = []
for _ in range(n):
    box.append(int(input()))

box.sort()
small = box[:n//2]
big = box[n//2:]

cnt = 0
while small:
    s = small.pop()
    if big[-1] >= s*2:
        big.pop()
        cnt += 1

print(n-cnt)