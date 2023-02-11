n=int(input())
lst=list(map(int,input().split()))
cnt=0
for ls in lst:
  if ls==1:
    continue
  for i in range(2,int(ls**0.5)+1):
    if ls%i==0:
      break
  else:
    cnt+=1

print(cnt)