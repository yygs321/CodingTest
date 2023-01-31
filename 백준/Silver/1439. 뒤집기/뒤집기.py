lst=input()
a=lst[0]
result=0
while lst:
    if lst[0]=='0':
        lst=lst.strip('0')
    else:
        lst=lst.strip('1')
    result+=1

print(result-1)