import heapq
from collections import defaultdict

q = int(input())
dic = defaultdict(list)
answer = 0
for _ in range(q):
    quest = list(input().split())

    if quest[0] == '1':
        dic[quest[1]] += list((map(int, quest[3:])))
        dic[quest[1]].sort()
    else:
        if dic[quest[1]]:
            answer += sum(dic[quest[1]][-int(quest[2]):])
            dic[quest[1]] = dic[quest[1]][:-int(quest[2])]

print(answer)