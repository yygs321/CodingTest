height=[]
for _ in range(9):
    height.append(int(input()))

sumV=sum(height)
diff=sumV-100

height.sort()
l,r=0,len(height)-1
tmp=0
result=set()
while l<r:
    if height[l]+height[r]>diff:
        r-=1
    elif height[l]+height[r]<diff:
        l+=1
    else:
        result.add(l)
        result.add(r)
        break

for idx,h in enumerate(height):
    if idx in result:
        continue
    print(h)