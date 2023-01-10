#A1
def is_symmetrical(a):
    n = a
    rev = 0
    while n!= 0:
        d = n%10
        rev = (rev*10) + d
        n = n//10
    #return a
    if (a == rev):
        return True
    else:
        return False
print(is_symmetrical(7227))

#A2
def multiply_nums(a):
    l = []
    ans =1
    b = a.replace(", ","")
    for i in b :
       l.append(int(i))
    for j in l:
        ans = ans*j
    return ans
print(multiply_nums("2, 3"))

#A3
def square_digits(a):
    l = []
    for i in str(a):
        l.append(int(i)**2)
    b = int("".join(map(str,l)))
    print(type(b))
    return b
print(square_digits(9119))

#A5
def mean(a):
    l = []
    for i in str(a):
        l.append(int(i))
    for j in l:
        b = sum(l)
    m = b//len(l)
    return m
print(mean(666))

