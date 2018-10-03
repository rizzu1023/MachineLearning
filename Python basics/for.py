



#wap to take start & end point from the user and print the range


no1=int(input("Enter first number"))
no2=int(input("Enter second number"))

for i in range(no2,no1-1,-1):
    print(i)


#wap to print fibonacci sersies up to n terms

num=int(input("Enter the number"))
a=0
b=1
print(a)
print(b)
for i in range(1,num-1):
    c=a+b
    print(c)
    #a=b
    #b=c
    a,b = b,c


#wap to find factorial of a given number

fact=int(input("Enter the number for factorial"))
res=1
for i in range(1,fact):
    res+=res*i

print("Factorial=",res)



#nested for loop

for i in range(1,5):
    for j in range(1,6):
        print("*",end='')
    print("\n",end='')