a,b=map(int,input().split())
if int("".join(reversed(str(a))))> int("".join(reversed(str(b)))): 
  print("".join(reversed(str(a))))
else: 
  print("".join(reversed(str(b))))