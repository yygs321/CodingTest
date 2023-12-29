n = int(input())

if n == 1:
    print(1)
    exit()

k = int((2*n)**0.5)
answer = 0
if k*(k+1)/2 > n:
    answer = k-1
else:
    answer = k

print(answer)
