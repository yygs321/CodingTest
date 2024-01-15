board = list(input().split('.'))
i = 0
answer = ''
for b in board:
    cnt = len(b)
    if cnt % 4 == 0:
        answer += 'A'*cnt+'.'
    elif (cnt % 4) % 2 == 0:
        answer += 'AAAA'*(cnt//4)+'BB'*((cnt % 4) // 2)+'.'
    elif cnt % 2 == 0:
        answer += 'B'*cnt+'.'
    else:
        print(-1)
        exit()


print(answer[:-1])