#A2
def simon_says(a,b):
    for i in range(len(a)):
        if (a[i] == b[i+1]):
        
            return True
        else: 
            return False
x = list(input("enter list: "))
y = list(input("enter list: "))
print(simon_says(x,y))

#A3
def society_name(a):
    s = ""
    for i in a:
        s = s + i[0]
    b = "".join(sorted(s))
    return b
print(society_name(["Harry", "Newt", "Luna", "Cho"]))

#A4

def is_isogram(a):
    l = []
    for i in a:
        if i in l:
            return False
        l.append(i)
    return True
    
print(is_isogram("password"))

#A5
def is_in_order(a):
    if a == sorted(a):
        return True
    else:
        return False
print(is_in_order("edabit"))

