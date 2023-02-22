#국어 영어 수학
N=int(input())
ls=[]
for _ in range(N):
    ls.append(input().split())

ls.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for l in ls:
    print(l[0])