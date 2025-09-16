name = input("Enter you Name: ")
age = int(input("Enter your Age: "))

if age > 18 and name == "Aadil":
    print(f"my name is {name}, and i am {age}, years old")
elif age > 18 and name == "Shah Ali":
    print(f"my name is {name}, and i am {age}, years old")
else:
    print("Name and age not match")