lst=list(input())
n=len(lst)
sum1,sum2=0,0

for i in range(n//2):
    sum1+=int(lst[i])

for i in range(n//2, n):
    sum2+=int(lst[i])

if sum1==sum2:
      print('LUCKY')
else:
      print('READY')
