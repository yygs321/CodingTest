# 최솟값이니까 - 뒤로 +가 나오는애들은 묶어서 한번에 빼는게 최소
# - 를 기준으로 나누면 +랑 숫자로 붙은애들은 그식 그대로 유지

line = input().split('-')

answer = 0
for idx, l in enumerate(line):
    tmp = l.split('+')
    num = 0
    for t in tmp:
        num += int(t.lstrip('0'))
    if idx == 0:
        answer += num
        continue
    answer -= num

print(answer)