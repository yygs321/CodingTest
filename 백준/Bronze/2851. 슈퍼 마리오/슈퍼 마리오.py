mushrooms=[]
for _ in range(10):
    mushrooms.append(int(input()))

tmp=0
answer=0
for mushroom in mushrooms:
    if tmp+mushroom<100:
        tmp+=mushroom
        answer=tmp
        continue

    if abs(100-tmp)<abs(100-(tmp+mushroom)):
        answer=tmp
    else:
        answer=tmp+mushroom
        #마지막까지 100을 안넘을 수 있기 때문에 여기서 출력하면 안됨
    break

print(answer)