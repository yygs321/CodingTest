from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    m = len(weak)
    
    for i in range(m):
        weak.append(weak[i] + n)
    
    for start in range(m):
        for friends in permutations(dist):
            count = 1
            arrival = weak[start] + friends[count - 1]
            for point in range(start, start + m):
                if arrival < weak[point]:
                    count += 1
                    if count > len(dist):
                        break
                    arrival = weak[point] + friends[count - 1]
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1
    return answer
