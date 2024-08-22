n = int(input())
storage = [0 for _ in range(1001)]

for _ in range(n):
    l, h = map(int, input().split())
    storage[l] = h

maxValue = max(storage)
max_idx = storage.index(maxValue)

tmp_l = 0
tmp_h = 0
result = 0
for i in range(max_idx+1):
    if storage[i] == 0:
        continue
    if tmp_h >= storage[i]:
        continue
    if tmp_l != 0:
        result += (i-tmp_l)*tmp_h
    tmp_l = i
    tmp_h = storage[i]

tmp_l = 0
tmp_h = 0
for i in range(1000, max_idx-1, -1):
    if storage[i] == 0:
        continue
    if tmp_h >= storage[i]:
        continue
    if tmp_l != 0:
        result += (tmp_l-i)*tmp_h
    tmp_l = i
    tmp_h = storage[i]

if max_idx != tmp_l:
    result += (tmp_l-max_idx+1)*maxValue
else:
    result += maxValue

print(result)