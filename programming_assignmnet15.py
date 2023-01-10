#A1
class divisible:
    def __init__(self,l):
        self.l = []
        
    def div(self,n):
        for i in range(n):
            if (i%7 == 0) and (i%5 == 0):
                self.l.append(str(i))
        print(",".join(self.l))
a = divisible(1)
x = int(input('enter n: '))
a.div(x)

#A2

class even:
    def __init__(self,l):
        self.l = []
        

    def evennum(self,n):
        for i in range(n):
            if (i%2 == 0):
                  self.l.append(str(i))
        print(",".join(self.l))

a = even(1)
b = int(input())
a.evennum(b)

#A3
n = int(input())
fib = [0, 1]
[fib.append(sum(fib[-2:])) for i in range(n)]
l=[]
for j in fib:
    l.append(str(j))
print(",".join(l))

#A4
a = input("enter emailid: ")
b = a.rsplit("@")
print("".join(b[0]))

#A5

class shape:
    def area(self):
        return "area = 0"
class square(shape):
    def __init__(self,l):
        self.l = l
    def area(self):
        return f"area = {self.l**2}"

x = shape()
print(x.area())
a = square(4)
print(a.area())

