MOD = 1000000007

n = int(input())
result = 0
arr = [0] * 3
s = input()

for i in range(n):
    if s[i] == 'W':
        arr[0] += 1
        arr[0] %= MOD
    elif s[i] == 'H':
        arr[1] += arr[0]
        arr[1] %= MOD
    elif s[i] == 'E':
        result += arr[2]
        arr[2] *= 2
        arr[2] += arr[1]
        arr[2] %= MOD
    result %= MOD

print(result)