graph=[list(map(int,input().split())) for _ in range(5)]

def check(k):
    for i in range(5):
        for j in range(5):
            if graph[i][j]==k:
                return (i,j)

def ysum():
    r=0
    for i in range(5):
        s=0
        for j in range(5):
            s+=graph[j][i]
        if s==0:
            r+=1
    return r

#5줄 대각선은 (i,i)만 가능
def lsum():
  s=0
  for i in range(5):
    s+=graph[i][i]
  return s

def rsum():
  s=0
  for i in range(5):
    s+=graph[4-i][i]
  return s

cnt=0
result=0
for i in range(5):
    lst=list(map(int,input().split()))
    for j in range(5):
        if cnt>=3:
          continue

        cnt=0
        result+=1
        
        x,y=check(lst[j])
        graph[x][y]=0

        #값 하나 나올때마다 그 행, 열만 확인하는게 아니라
        #모든 행, 열값의 빙고수를 다 다시 세야함 -> cnt=0으로 초기화하기 때문에
        
        #행 합  
        for k in range(5):
          if sum(graph[k])==0:
              cnt+=1
        #열 합
        cnt+=ysum()
        #왼쪽 대각선
        if lsum()==0:
            cnt+=1
        #오른쪽 대각선
        if rsum()==0:
            cnt+=1

print(result)