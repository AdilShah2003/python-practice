num1 = int(input("Enter your 1st Number: "))
num2 = int(input("Enter your 2nd Number: "))
num3 = int(input("Enter your 3rd Number: "))

if num1 > num2 and num1 > num3:
    print("Num1 Grestest num1 and num2")
elif num2 > num1 and  num2 > num3:
    print("Num2 Grestest num1 and num3")
elif num3 > num1 and  num3 > num2:
    print("Num3 Grestest num1 and num2")
else:
    print("All number is equal")
