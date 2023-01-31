# Python
def dn(n2):
    if n2 <= 9:
        n = n2 + n2
    elif n2 <= 99:
        strn = str(n2)
        n = n2 + int(strn[0]) + int(strn[1])
    elif n2 <= 999:
        strn = str(n2)
        n = n2 + int(strn[0]) + int(strn[1]) + int(strn[2])
    else:
        strn = str(n2)
        n = n2 + int(strn[0]) + int(strn[1]) + int(strn[2]) + int(strn[3])
    return n

dn_list = list()

for i in range(10000):
    dn_list.append(dn(i))
    
print_list = list(set(range(10000)) - set(dn_list))
print_list.sort()

for print_i in print_list:
    print(print_i)


