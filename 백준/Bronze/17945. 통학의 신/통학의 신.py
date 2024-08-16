a, b = list(map(int, input().split()))

result=[]
for i in range(-1000, 1001):
    if i*i + 2*a*i + b == 0:
        result.append(i)
        
print(*result)