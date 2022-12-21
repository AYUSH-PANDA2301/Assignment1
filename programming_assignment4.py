#A1
a=int(input())
b=1
for i in range(1,a+1):
   b = b*i
print(b)
###################
#A2

a = int(input('enter number for which you need the multiplication table: '))
for i in range(1,11):
    print(f'{a}*{i} = ' , a*i)
########################################

#A4

a = int(input())
sum = 0
c=a
while(a>0):
    b=a%10
    sum+=b*b*b
    a=a//10
if c == sum:
    print("armstrong")
else:
    print('not armstrong')
#######################################
#A5

a=int(input())
b=int(input())

for i in range(a,b+1):
    sum=0
    c=i
    while(i>0):
       d=i%10
       sum+=d*d*d
       i=i//10
    if c == sum:
     print(c)
#############################
#A6

a=int(input())
sum = a*(a+1)//2
print(sum)

#or
a=int(input())
sum =0
for i in range (1,a+1):
    sum+=i
print(sum)

##############################
#A3
a1=int(input('enter first digit'))
a2=int(input('enter second digit'))
n=int(input('enter limit'))
b=0
while(b<n):
    print(a1)
    sum=a1+a2
    a1=a2
    a2=sum
    b+=1




