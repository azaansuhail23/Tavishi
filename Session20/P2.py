age = int(input("Enter your age "))
grade=int(input("Please enter your grade"))

if age <= 10:
    print("Kid")
elif age > 10 and age <= 18:
    if grade=="8":
        print("Teenage 8 grade")
else:
    print("Adult")
