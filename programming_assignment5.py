#A4
a=input()
print('ascii value of a :', ord(a))
#####################################

#A5
n1 = float(input('enter first operand : '))
n2 = float(input('enter second operand : '))
a = input("enter operator: ")

if a == '+':
    print(n1+n2)
elif a == '-':
    print(n1-n2)
elif a == '*':
    print(n1*n2)
elif a == '/':
    print(n1//n2)
#########################################
#A1
x = int(input())
y = int(input())
if x > y:
       n = x
else:
       n = y

while(True):
       if((n % x == 0) and (n % y == 0)):
           lcm = n
           break
       n += 1
print(lcm)
#######################################
#A2
x = int(input())
y = int(input())
if x > y:
        n = y
else:
        n = x
for i in range(1, n+1):
    if((x % i == 0) and (y % i == 0)):
        hcf = i 
print(hcf)    
#######################################
#A3
## decimal to binary
a=int(input())
print(bin(a)[2:])
##############
## octal to hexadecimal
a=int(input("enter octal number"))
print("hexadecimal number is : ",hex(a))