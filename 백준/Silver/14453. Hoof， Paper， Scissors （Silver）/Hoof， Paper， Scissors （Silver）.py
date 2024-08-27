n = int(input())
john = [0]
for _ in range(n):
    x = input()
    if x == 'H':
        john.append(0)
    elif x == 'P':
        john.append(1)
    else:
        john.append(2)

# 이길 수 있는 값
john = [(x+1) % 3 for x in john]

# 이길 수 있는 값의 개수
prefix_count = [[0, 0, 0] for _ in range(n+1)]
for i in range(1, n+1):
    idx = john[i]

    prefix_count[i] = prefix_count[i-1][:]
    prefix_count[i][idx] += 1

suffix_count = [[0, 0, 0] for _ in range(n+2)]
for i in range(n, 0, -1):
    idx = john[i]
    suffix_count[n-i+1] = suffix_count[n-i][:]
    suffix_count[n-i+1][idx] += 1

ans = 0
for i in range(1, n):
    ans = max(ans, max(prefix_count[i])+max(suffix_count[n-i]))

print(ans)