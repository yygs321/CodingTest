alpha="abcdefghijklmnopqrstuvwxyz"
str=input()
for a in alpha:
  if a in str:
    print(str.index(a), end=" ")
  else:
    print(-1, end=" ")