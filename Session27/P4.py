age=int(input("Enter the age "))


if age<=10:
    print("Kid can ride ")
    print("Teenage can ride ")
    print("Adult can ride ")
    
elif age>10 and age<=18:
    print("Teenage can ride ")
    print("Adult can ride ")
else:
    print("Only Adult can ride")