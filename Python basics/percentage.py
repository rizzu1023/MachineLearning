#write a programe to take percentage from user & print first class if % is 60 or above 60, print Second class if % is in between
#40 to 60, print KT if % is less than 40


perc=input("Enter the percentage")

perc=int(perc)


if(perc>=60):
    print("First Class")
elif(perc>=40 and perc<=60):
    print("Second Class")
else:
    print("KT")