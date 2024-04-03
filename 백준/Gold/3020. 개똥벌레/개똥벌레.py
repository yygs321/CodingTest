n, h = map(int, input().split())

# 종유석 정보 저장
down = [0] * (h+1)
# 석순 정보 저장
up = [0] * (h+1)

for i in range(n):
    # 장애물 크기
    x = int(input())

    if (i % 2 == 0):
        down[x] += 1
    else:
        up[x] += 1

# 인덱스를 역순으로 누적합을 계산
for i in range(h-1, 0, -1):
    # 높이가 i+1인건 높이 i에도 영향을주기 때문에 i+1 갯수를 i 에게도 넣어줌
    down[i] += down[i+1]
    up[i] += up[i+1]

min_val = n  # 최대가 n
cnt = 0

for i in range(1, h+1):

    if (up[i] + down[h - i + 1]) < min_val:
        min_val = up[i] + down[h - i + 1]
        cnt = 1

    elif (min_val == up[i] + down[h - i + 1]):
        cnt += 1

print(min_val, cnt)