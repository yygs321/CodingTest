# 0이 없으면 -1
# 끝은 0으로 두고 나머지가 3의 배수여야함
# 3의 배수 -> 합이 3의 배수여야함
n = int(input())
tmp = list(str(n))
tmp.sort(reverse=True)
lst = [int(i) for i in tmp]
if 0 not in lst:
    print(-1)
    exit()
if sum(lst) % 3 != 0:
    print(-1)
    exit()

print(''.join(tmp))