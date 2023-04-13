lst=input()
while lst[0]!='#':
    mo=['a','e','i','o','u']
    cnt=0
    for ls in lst.lower():
        if ls in mo:
            cnt+=1
    print(cnt)
    lst=input()