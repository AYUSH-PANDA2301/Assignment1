#A1
def amplify(a):
    l = []
    for i in range(1,a+1):
        if (i%4 == 0):
            l.append(i*10)
        else:
            l.append(i)
    return l
print(amplify(25))

#or
def amplify(a):
      l = [i*10 if i%4 == 0 else i for i in range(1,a+1) ]
      return l
print(amplify(25))

#A3
class circle:
    def __init__(self,radius):
        self.radius = radius
    def getArea(self):
        return 3.14*(self.radius)**2
    def getPerimeter(self):
        return 2*3.14*self.radius

circy = circle(11)
print(circy.getArea())
print(circy.getPerimeter())

#A4
def sort_by_length(a):
    a.sort(key = len)
    return a
print(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))

#A5
def is_triplet(a,b,c):
    l = []
    x = []
    y = []
    l.append(a)
    x.append(b)
    y.append(c)
    l+=x+y
    l.sort()
    if (l[0]**2 + l[1]**2 == l[2]**2):
        return True
    else:
        return False
print(is_triplet(3,1,2))

#or
def is_triplet(a, b, c):
    if a > b and a > c:
        return a**2 == b**2 + c**2
    elif b > a and b > c:
        return b**2 == a**2 + c**2
    else:
        return c**2 == a**2 + b**2
