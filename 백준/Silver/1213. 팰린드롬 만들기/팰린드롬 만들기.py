# 대칭이 되려면 홀수개인 문자열이 1개 이하여야함
# 정렬된 순으로 대칭
from collections import Counter

name = input().rstrip()
cnt = 0  # 홀수 갯수 확인
result = ''
mid = ''  # 중간에 들어갈 값
for k, v in list(Counter(name).items()):
    if v % 2 != 0:
        cnt += 1
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()

        mid = k

for k, v in sorted(Counter(name).items()):
    result += (k*(v//2))  # 홀수 개면 가운데 넣을 1개 빼고 나머지갯수의 반개만큼 들어감

print(result+mid+result[::-1])