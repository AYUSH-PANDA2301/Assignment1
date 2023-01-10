#A4
import re
def index_of_caps(a):
    l = []
    for i in range(len(a)):
        if(bool(re.match('[A-Z]',a[i]))):
            l.append(i)
    return l

print(index_of_caps("eDaBiT"))

#A5
def find_even_nums(a):
    l = [i for i in range(1,a+1) if i%2 == 0]
    return l
print(find_even_nums(8))

#A2
def reverse(a):
    if a == True:
        return False
    elif a == False:
        return True
    else:
        return "boolean expected"
print(reverse(None))

#A1
def double_char(a):
    str = ""
    for i in range(len(a)):
        str += a[i]*2
    return str
print(double_char("string"))