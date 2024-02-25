from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        comb_list = []

        for order in orders:
            comb_list += combinations(sorted(order), c)

        #개수 많은 순으로 정렬된 배열 리턴
        #  ex) ((a,b),3) : (a,b)조합이 3개 
        count = Counter(comb_list).most_common()
        answer += [l[0] for l in count if (l[1] == count[0][1] and l[1] > 1)]


    answer = [''.join(a) for a in sorted(answer)]

    return answer