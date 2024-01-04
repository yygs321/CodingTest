a, b = map(int, input().split())
anum = []
bnum = []
maxA, maxB, minA, minB = 0, 0, 0, 0


def cal(a):
    mx, mi = 0, 0
    for idx, num in enumerate(list(str(a))[::-1]):
        if int(num) == 5:
            mx += 6*(10**idx)
            mi += 5*(10**idx)
            continue
        if int(num) == 6:
            mx += 6*(10**idx)
            mi += 5*(10**idx)
            continue
        mx += int(num)*(10**idx)
        mi += int(num)*(10**idx)

    return (mx, mi)


maxA, minA = cal(a)
maxB, minB = cal(b)
print(minA+minB, maxA+maxB)