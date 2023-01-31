import sys
while True:
    try: 
        a,b=sys.stdin.readline().split()
        a=int(a)
        b=int(b)
        print(a+b)
    except:
        break