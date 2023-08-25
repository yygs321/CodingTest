#같은 양의 물 -> 합칠 수 있음
#상점에서 1L 물병 구매가능
#비어있지 않은 K개이하의 물병을 만들기위해 구매해야할 물병 최소개수
n,k=map(int,input().split())
bottle=0
result=-1

lst=list(reversed(format(n,'b').rstrip()))
if lst.count('1')<=k:
    result=0
else:
    for i in range(len(lst)-1,-1,-1):
        if lst[i]=='1':
            bottle +=1
        if bottle==k:
            result=2**i - sum([2**int(j) for j in range(0,i) if lst[j]=='1'])
            break

print(result)
