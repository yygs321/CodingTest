n = int(input())
rooms = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0
for room in rooms:
    answer += 1
    room -= b
    if room > 0:
        answer += room//c
        if room % c > 0:
            answer += 1

print(answer)
