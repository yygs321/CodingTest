#SW 4013
#4개 자석 k번 돌린 전부 돌린 후 점수
# 점수: n극 0점, s극 2의 자석번호 제곱수만큼1,2,4,8(0~3 제곱)
#시계방향 1 반시계방향 -1
#n극 0 s극 1
def point_check(pnt): #접하는 지점 
    if pnt-2<0:
        pnt+=8
    return pnt-2

def rotate(m,dir):
    visited[m]=True
    p=point[m] #기존 포인트값
    if dir==1: #시계방향일때 왼쪽으로(작아짐)
        if point[m]==0:
            point[m]=7
        else:
            point[m]-=1

        #접하는 면이 자석이 반대일때만 실행
        #위에서 point바뀌기 전값으로 생각해야함
        if m+1<=3 and magnet[m][(p+2)%8] != magnet[m+1][point_check(point[m+1])]: #우측 자석
            if visited[m+1]==False:
                rotate(m+1, -1)
        if m-1>=0 and magnet[m][point_check(p)]!=magnet[m-1][(point[m-1]+2)%8]:
            if visited[m-1]==False:#좌측 자석
                rotate(m-1,-1)
      
    else: #반시계방향일때 오른쪽으로(커짐)
        point[m]=(point[m]+1)%8
        
        #자석 반대면 실행
        if m+1<=3 and magnet[m][(p+2)%8]!=magnet[m+1][point_check(point[m+1])]: 
            if visited[m+1]==False:
                rotate(m+1, 1)
        if m-1>=0 and magnet[m][point_check(p)]!=magnet[m-1][(point[m-1]+2)%8]:
            if visited[m-1]==False:
                rotate(m-1,1)



magnet=[]
for i in range(4):
    #magnet[0] 위치가 점수계산할 위치
    magnet.append(list(map(int,input().rstrip())))

k=int(input())

rotation=[]
for j in range(k):
    #자석번호, 회전방향 [a,b]
    a,b=map(int,input().split())
    a-=1 #0~3번 자석으로 인덱스=이름 맞추기
    rotation.append([a,b])

point=[0]*4 #점수위치

#회전
for rt in rotation:
    visited=[False]*4
    m,dir=rt #자석번호, 방향
    rotate(m,dir)

result=0
for idx, p in enumerate(point):
    if magnet[idx][p]==0: continue #n극 0점
    else: 
        result+=2**idx

print(result)