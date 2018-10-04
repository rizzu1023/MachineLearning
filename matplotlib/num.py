import numpy as np

# a=np.array([4,3,9])
# a=np.arange(0,12)
# a=np.arange(12).reshape(4,3)

x=np.arange(9).reshape(3,3)
y=np.arange(9).reshape(3,3)
a=x*y
# print(x)
# print(y)
# print(a)

no=int(input("Enter no of elements").strip())
li=list(map(int,input("Enter elements").rstrip().split()))
print(li)
# n=int(input("Enter no of elements"))
# li=[]
# for i in range(0,n):
#     element=input("Enter element")
#     li.append(element)

# print(li)

# print(type(a))
