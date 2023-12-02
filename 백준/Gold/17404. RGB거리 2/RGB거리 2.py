import copy

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')
for k in range(3):
    tmp = copy.deepcopy(rgb)
    if k == 0:
        tmp[1][0] = min(tmp[0][1], tmp[0][2]) + tmp[1][0]
        tmp[1][1] = tmp[0][2] + tmp[1][1]
        tmp[1][2] = tmp[0][1] + tmp[1][2]
    elif k == 1:
        tmp[1][0] = tmp[0][2] + tmp[1][0]
        tmp[1][1] = min(tmp[0][0], tmp[0][2]) + tmp[1][1]
        tmp[1][2] = tmp[0][0] + tmp[1][2]
    elif k == 2:
        tmp[1][0] = tmp[0][1] + tmp[1][0]
        tmp[1][1] = tmp[0][0] + tmp[1][1]
        tmp[1][2] = min(tmp[0][0], tmp[0][1]) + tmp[1][2]
    for i in range(2, n):
        tmp[i][0] = min(tmp[i-1][1], tmp[i-1][2])+tmp[i][0]
        tmp[i][1] = min(tmp[i-1][0], tmp[i-1][2])+tmp[i][1]
        tmp[i][2] = min(tmp[i-1][0], tmp[i-1][1])+tmp[i][2]

    answer = min(answer, tmp[n-1][k])

print(answer)