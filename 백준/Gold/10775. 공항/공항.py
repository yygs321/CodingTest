#1,g까지 게이트
#1, i번째게이트 중 하나에 도킹
#앞 비행기 도킹 불가 -> break
#최대 도킹 수
def union(x,y):
    xroot=find(x)
    yroot=find(y)
    if xroot<=yroot:
        root[yroot]=xroot
    else:
        root[xroot]=yroot

def find(x):
    if x!=root[x]:
        root[x]=find(root[x])
    return root[x]

g=int(input())
p=int(input())
plane=[]
for _ in range(p):
    plane.append(int(input()))

root=[i for i in range(g+1)]
cnt=0

for pp in plane:
    px=find(pp) 
    if px==0: # 가능한 게이트가 0이면 이후 전부 도킹 불가
        break
    union(px,px-1) # 다음 비행기가 사용할 수 있는 가장 큰 게이트 번호로 바꾼다
    cnt+=1

print(cnt)