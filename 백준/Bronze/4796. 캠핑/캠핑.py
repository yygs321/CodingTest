L, P, V = map(int, input().split())
case = 0
while L != 0 or P != 0 or V != 0:
    case += 1
    holiday = 0
    holiday += (V//P)*L
    V %= P
    if L <= V:
        holiday += L
    else:
        holiday += V

    print(f'Case {case}: {holiday}')

    L, P, V = map(int, input().split())
