#A5
def missing_num(a):
    for i in range(1,10):
        if i not in a:
            return i
print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))

#A2
def add_indexes(a):
   l = [a[i]+i for i in range(len(a))]
   return l
print(add_indexes([0, 0, 0, 0, 0]))

#A4
def triangle(a):
    l = []
    for i in range(1,a+1):
        l.append(i*(i+1)//2)
    return l
print(triangle(6))
