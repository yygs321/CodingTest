from itertools import permutations 

def operate(n1,n2,o):
    if o=='+':
        return n1+n2
    elif o=='-':
        return n1-n2
    elif o=='*':
        return n1*n2
    else:
        return int(n1/n2)
          
n=int(input())
operator="+-*/"
num=list(map(int,input().split())) #숫자 
lst=list(map(int,input().split())) #연산자

op=""

for idx,ls in enumerate(lst):
    op+=operator[idx]*ls

#set으로 중복 제거
#연산자 개수: n-1
pmt=set(permutations(op,n-1))

first=num.pop(0) #하나 줄여서 연산자랑 개수 맞춤

max_val,min_val=-1e9, 1e9
for pm in pmt:
    result=first #매연산 돌아갈때 첫숫자부터 다시 계산
    for n, p in zip(num, pm):
        result=operate(result, n, p)
      
    max_val=max(max_val,result)
    min_val=min(min_val,result)

print(max_val)
print(min_val)