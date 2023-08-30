from collections import defaultdict

n=int(input())
tree=list(map(int,input().split()))
height=list(map(int,input().split()))
dic=defaultdict(list)
for idx, two_value in enumerate(zip(tree, height)):
    dic[idx].append(two_value[1])
    dic[idx].append(two_value[0])

val=list(dic.values())
val.sort()

result=0
result+=val[0][1]
for i in range(n-1,0,-1):
    result+=val[i][1]+val[i][0]*i

print(result)