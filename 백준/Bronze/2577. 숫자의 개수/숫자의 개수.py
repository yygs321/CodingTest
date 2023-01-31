A=int(input())
B=int(input())
C=int(input())
result=A*B*C
string=str(result)
for i in range(10):
    print(string.count(str(i)))