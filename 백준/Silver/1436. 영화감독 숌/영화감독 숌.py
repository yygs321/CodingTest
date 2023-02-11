n=int(input())
num=0
cnt=0

while True:
    if '666' in str(num):
        cnt+=1
    if cnt==n: #666이 들어가는 n번째 수
        print(num)
        break
      
    num+=1