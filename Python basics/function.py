
def display():
    print("Inside display function")

#display()

def addition(a,b):
    return a+b

#print(addition(5,6))

#wap to find factorial of a given number using function


def facto(no):
    res=1
    for i in range(1,no+1):
        res*=i
    return res

print(facto(4))