#묶은 수: 서로 곱한 후 더함
def quick(lst,start,end):
    if start>=end: #lst길이가 1이면 종료
        return

    pivot=start
    left=start+1 #pivot 다음 값부터 확인
    right=end

    while left<=right:
        while left<=end and lst[left]<=lst[pivot]:
            left+=1
        while right>start and lst[right]>=lst[pivot]:
            right-=1

        if left<=right: #엇갈리지 않은경우
            lst[left], lst[right]= lst[right], lst[left]
        else:
            lst[right], lst[pivot]= lst[pivot], lst[right]

    quick(lst, start, right-1)
    quick(lst, right+1, end)

n=int(input())
lst=[]
result=0

for _ in range(n):
    lst.append(int(input()))

quick(lst, 0, n-1)

idx=n-1
cnt=1 #0 없으면 음수 곱해서 더할 수 있게 1
flag=0 #첫 음수확인
while idx>=0:
    if lst[idx]==0:
        #0이랑 가장 작은 음수값이 존재하면 두 값 곱해서 없애버림
        #음스확인
        idx-=1
        cnt=0 #0이 있으면 0 -> 곱해서 음수 없앨 수 있게
        continue

    if lst[idx]<0 and flag==0:
        flag=1
        if len(lst[:idx+1])%2!=0 : #음수 개수가 홀수면
            result+=lst[idx]*cnt #0이 있으면 없애버리도록
            idx -= 1
            #마지막값끼리 곱해지면 커지므로 마지막값을 지울 순 없음
        continue

    if lst[idx]*lst[idx-1]>lst[idx]+lst[idx-1] and idx>=1:
        result+=lst[idx]*lst[idx-1]
        idx-=2
    else:
        result+=lst[idx]
        idx-=1

print(result)