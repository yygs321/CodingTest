n = int(input())
numbers = list(map(int, input().split()))

result = [1 for _ in range(n)]

for i, num in enumerate(numbers):
    if i == 0:
        continue

    for j in range(i-1, -1, -1):
        if numbers[j] > num:
            result[i] = max(result[i], result[j]+1)
        elif numbers[j] == num:
            result[i] = max(result[i], result[j])

print(max(result))
