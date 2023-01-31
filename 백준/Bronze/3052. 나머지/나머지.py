a=[]
for i in range(10):
    a.append((int(input()))%42)
b=[]
b.append(a[0])
cnt=1
for i in range(9):
    if a[i+1] in b:
        pass
    else:
        b.append(a[i+1])
        cnt+=1
print(cnt)