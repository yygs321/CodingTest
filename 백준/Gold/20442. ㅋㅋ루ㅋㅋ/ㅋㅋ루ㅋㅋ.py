# 가장 긴 부분수열 길이
# 양끝에서부터 R이 나올때마다 K개수 비교해서 체크
# 투포인터
kkr = input().strip()
lp = []
rp = []
cnt = 0

for i in kkr:
    if i == 'K':
        cnt += 1
    else:
        lp.append(cnt)

cnt=0
for i in kkr[::-1]:
    if i == 'K':
        cnt += 1
    else:
        rp.append(cnt)
rp.reverse()

# len(lp), len(rp)는 R의 개수가 됨
l, r = 0, len(lp) - 1
answer = 0
while l <= r:
    # r-l+1 : R의 개수
    # 양끝에 k가 붙어야하므로 왼쪽,오른쪽 K개수 중 작은 값 만큼만 가능
    answer = max(answer, r - l + 1 + 2 * min(lp[l], rp[r]))
    # K의 개수가 작은 쪽을 이동하여 다음 R이 나올때까지 탐색
    if lp[l] < rp[r]:
        l += 1
    else:
        r -= 1

print(answer)