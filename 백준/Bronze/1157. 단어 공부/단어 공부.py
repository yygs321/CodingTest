st=input().upper()
st_copy=list(set(st))
cnt=[]
result=""

for s in st_copy:
    cnt.append(st.count(s))

if cnt.count(max(cnt))>1:
      print("?")
else:
      print(st_copy[cnt.index(max(cnt))])