#10000 이하: weak
#100000 이하 normal
#1000000 이하 strong
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
power=[]
name=[]
for i in range(n):
    pname, maxPower=input().split()
    if power and power[-1]==int(maxPower):
        continue
    name.append(pname)
    power.append(int(maxPower))


def binary(check):
    left=0
    right=len(power)-1
  
    while left <= right:
        mid=(left+right)//2
        if check<=power[mid]:
            right=mid-1
        elif check >power[mid]:
            left=mid+1
    print(name[right+1])
  
for i in range(m):
    check=int(input())
    binary(check)