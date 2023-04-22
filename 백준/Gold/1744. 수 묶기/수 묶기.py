n=int(input())
lst=[]
result=0

for _ in range(n):
    lst.append(int(input()))

lst.sort()

idx=n-1
cnt=1 #0 없으면 음수 곱해서 더할 수 있게 1
flag=0 #첫 음수확인
while idx>=0:
    if lst[idx]==0:
        idx-=1
        cnt=0 #0이 있으면 0 -> 곱해서 음수 없앨 수 있게
        continue

    if lst[idx]<0 and flag==0: #처음으로 음수 나왔을 경우(음수 중 가장 큰값)
        flag=1
        if len(lst[:idx+1])%2!=0 : #음수 개수가 홀수면
            result+=lst[idx]*cnt #0이 있으면 없애고 있으면 더함
            idx -= 1
        continue

    if lst[idx]*lst[idx-1]>lst[idx]+lst[idx-1] and idx>=1:
        result+=lst[idx]*lst[idx-1]
        idx-=2
    else:
        result+=lst[idx]
        idx-=1

print(result)