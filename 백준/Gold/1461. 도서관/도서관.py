# 제일 멀리 있는게 맨 마지막
# 맨마지막 경우가 아니면 결국 m개씩 들고갈때 왕복 왔다갔다 해야함
# 0점을 지나갈거면 무조건 새로 m개 들고 움직이는게 이득
n, m = map(int, input().split())
book = list(map(int, input().split()))
bookA = [book[i] for i in range(n) if book[i] > 0]
bookB = [-book[i] for i in range(n) if book[i] < 0]
bookA.sort(reverse=True)
bookB.sort(reverse=True)

result = []
i = 0
while i < len(bookA):
    result.append(bookA[i])
    i += m

i = 0
while i < len(bookB):
    result.append(bookB[i])
    i += m

result.sort()
answer = 0
answer += result.pop()
answer += 2*(sum(result))
print(answer)