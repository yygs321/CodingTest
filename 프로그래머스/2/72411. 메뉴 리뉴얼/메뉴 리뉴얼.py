from collections import Counter, defaultdict
from itertools import combinations
def solution(orders, course):
    results = defaultdict(list)
    combi=[]
    course=set(course)

    for order in orders:
        order=sorted(list(order))
        for i in range(2,len(order)+1):
            combi+=list(combinations(order,i))
    cnt_combi=Counter(combi)
    for key,val in sorted(list(cnt_combi.items()), key=lambda x:x[1], reverse=True):
        if val<2:
            continue
        n= len(key)
        if n in course:
            if not results[n]:
                results[n]=[(''.join(key), val)]
                continue
            if results[n][0][1]<=val:
                results[n].append((''.join(key), val))

    answer=[]
    for result in list(results.values()):
        for r in result:
            answer.append(r[0])
    return sorted(answer)