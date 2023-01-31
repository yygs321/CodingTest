#8958 (해설봤음)
n=int(input())
for i in range(n):
    a=input()
    O_Score=0
    X_Score=0
    Total_Score=0
    TS=[]
    for B in a:
        if B=="O":
            O_Score+=1
            Total_Score += O_Score
        else:
            X_Score=0
            O_Score=0
    print(Total_Score)