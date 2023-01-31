H,M = map(int, input().split())
if H>= 0 and M>=45:
    print(H,(M-45))
elif H<0 and M>=45:
    print((H+24),(M-45))
elif H>0 and M<45:
    print((H-1),(60-45+M))
else:
    print((H-1+24),(60-45+M))