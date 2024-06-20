def solution(elements):
    n = len(elements)
    result = set()

    for i in range(n):
        tmp = elements[i]
        result.add(tmp)
        for j in range(i+1, i+n):
            tmp += elements[j%n]
            result.add(tmp)
    return len(result)