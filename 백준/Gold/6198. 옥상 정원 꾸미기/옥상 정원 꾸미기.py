n = int(input())
buildings = [int(input()) for _ in range(n)]
stack = []
answer = 0

for bd in buildings:
    while stack and stack[-1] <= bd:
        stack.pop()

    answer += len(stack)
    stack.append(bd)

print(answer)