n = int(input())

nums = list(map(int,input().split()))

pos = [0]*(len(nums)+1)

tmp = 1
cnt = 1

for i in range(0,n):
    pos[nums[i]] = i

for i in range(1,n-1):
    if pos[i] < pos[i+1]:
        cnt += 1
        if(cnt > tmp):
            tmp = cnt
    else:
        cnt = 1

print(n-tmp)