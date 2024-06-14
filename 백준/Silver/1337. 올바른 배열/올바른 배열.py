n = int(input())
nums = [int(input()) for _ in range(n)]

result = float('inf')
for num in nums:
    for i in range(-4, 5):
        tmp = 0
        for j in range(5):
            if num+i+j not in nums:
                tmp += 1
        result = min(result, tmp)

print(result)