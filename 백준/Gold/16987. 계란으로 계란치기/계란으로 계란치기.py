#계란으로 계란을 깨면 -> 계란 내구도 : 상대계란 무게 만큼 둘다 깎임
# 내구도가 0이하가 되면 계란 깨짐
# 왼쪽부터 일렬로 한번씩만 계란을 쳐서 최대한 많은 계란을 깨는 문제

#가장 왼쪽계란을 들기
#손에든 계란이 깨지거나, 깨지징않은 계란 없으면 넘어감
#가장 오른쪽 계란이 끝나면 종료
#최대 몇개 계란 
def crack(cnt, egg):
  global result
  if cnt==n:
    r=0
    for e in egg:
      if e[0]<=0: r+=1

    result=max(result,r)
    return

  if egg[cnt][0]<=0: #자기가 깨진 경우
    crack(cnt+1, egg)
    return

  #자기말고 다 깨진 경우
  all=0
  for i in range(n):
    if i==cnt: continue
    if egg[i][0]>0: 
      all=1
      
  if all==0: #전부 다 깨진 경우
    result=max(result, n-1)
    return
    
  for j in range(n):
    if cnt==j or egg[j][0] <=0:
      continue

    #계란 치기
    egg[cnt][0]-=egg[j][1]
    egg[j][0]-=egg[cnt][1]
    crack(cnt+1, egg)

    #복원
    egg[cnt][0]+=egg[j][1]
    egg[j][0]+=egg[cnt][1]
     

n=int(input())
egg=[]
result=0

for i in range(n):
  #내구도, 무게
  a,b=map(int,input().split())
  egg.append([a,b])

result=0
crack(0,egg)
print(result)