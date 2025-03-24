from collections import defaultdict

def solution(weights):
    answer = 0
    weights.sort()
    
    weights_dict = defaultdict(float)
    ratio = [1/1, 1/2, 2/3, 3/4]
    
    for w in weights:
        for r in ratio:
            answer += weights_dict[r * w]
        weights_dict[w] += 1

    return answer

