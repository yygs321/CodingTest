n = int(input())
alst = list(map(int, input().split()))
m = int(input())
blst = list(map(int, input().split()))


def solution(a, b, result):
    if (not a) or (not b):
        return result

    tmp1 = max(a)
    tmp2 = max(b)

    idx1 = a.index(tmp1)
    idx2 = b.index(tmp2)

    if tmp1 == tmp2:
        result.append(tmp1)
        solution(a[idx1+1:], b[idx2+1:], result)
    elif tmp1 > tmp2:
        a.pop(idx1)
        solution(a, b, result)
    else:
        b.pop(idx2)
        solution(a, b, result)


result = []
solution(alst, blst, result)

print(len(result))
print(*result)