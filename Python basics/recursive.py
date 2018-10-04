def facto(no):
    if (no==1):
        return 1
    else:
        return (no*facto(no-1))


# no=int(input("Enter a Number"))
# print("Factorial=",facto(no))


def pow(base,index):
    if (index==1):
        return base
    elif(base==0):
        return 1
    else:
        return base*pow(base,index-1)


base=int(input("Enter base"))
index=int(input("Enter index"))
print("Answer=",pow(base,index))