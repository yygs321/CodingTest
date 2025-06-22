from collections import defaultdict

def solution(clothes):
    answer = 1
    dict=defaultdict(int)
    for c in clothes:
        name,type=c
        dict[type]+=1
    
    for val in list(dict.values()):
        answer*=(val+1)
    answer-=1

    return answer