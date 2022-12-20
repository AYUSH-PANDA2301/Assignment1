#A1
a=int(input())
if a>0:
    print("positive")
elif a<0:
    print('negative')
else:
    print("it is zero")
##############################

#A2
a=int(input())
if a%2==0:
    print("number is even")
else:
    print("number is odd")
#################################
#A3

a=int(input())
if(a%400 == 0) and (a%100 == 0):
    print("it is a leap year")
elif(a%4 == 0) and (a%100 !=0):
    print('it is a leap year')
else:
    print('it is not a leap year')
#######################################

#A4

a=int(input())
if a>1:
    for i in range (2,a):
        if a%i == 0:
            print("not a prime number")
        else:
            print('it is prime')
#########################################

#A5

for i in range (1,10001):
    count = 0
    for j in range(2,(i//2+1)):
        if i%j == 0:
            count +=1
            break
    if (count == 0 and i!=1):
        print(i)