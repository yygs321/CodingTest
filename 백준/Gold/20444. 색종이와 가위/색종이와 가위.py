n,k=map(int,input().split())
answer=0
#가로로 자른 횟수 rowCut
#세로로 자른 횟수 colCut
#-> 나오는 종이 조각 (rowCut+1)*(colCut)
#rowCut/ colCut 개수 대칭 -> n//2까지만 확인하면 됨.
l=0
r=n//2

while l<=r:
    rowCut=(l+r)//2
    colCut=n-rowCut

    piece=(rowCut+1)*(colCut+1)

    if k==piece:
        answer=1
        break
    elif k<piece:
        r=rowCut-1
    else:
        l=rowCut+1

if answer==1:
    print("YES")
else:
    print("NO")