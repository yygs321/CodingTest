#입력 없을 시  종료 -> while 안에 try-except

while True:
    try:
        x = int(input())*10000000
        n = int(input())
        lego = []
        for _ in range(n):
            lego.append(int(input()))

        lego.sort()
        l = 0
        r = len(lego)-1
        result = 0
        while l < r:
            if lego[l]+lego[r] > x:
                r -= 1
                continue
            elif lego[l]+lego[r] < x:
                l += 1
                continue
            else:
                result = 1
                break

        if result:
            print(f'yes {lego[l]} {lego[r]}')
        else:
            print('danger')

    except:
        break