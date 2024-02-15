from collections import defaultdict

n = int(input())
m = 0
all_lst = []
alpha = defaultdict(int)
for _ in range(n):
    tmp = list(input().rstrip())
    all_lst.append(tmp)

    for i in range(len(tmp)-1, -1, -1):
        alpha[tmp[i]] += 10**(len(tmp)-i-1)
    m = max(m, len(tmp))

alpha_lst = sorted(alpha.items(), key=lambda x: x[1], reverse=True)
num = 9
answer = 0
for a in alpha_lst:
    answer += num*a[1]
    num -= 1

print(answer)