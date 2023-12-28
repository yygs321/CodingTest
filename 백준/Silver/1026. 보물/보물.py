n = int(input())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

alist.sort(reverse=True)
blist.sort()

s = 0
for a, b in zip(alist, blist):
    s += a*b

print(s)