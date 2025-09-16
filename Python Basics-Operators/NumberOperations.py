
num1 = int(input("Enter your 1st Number: "))
num2 = int(input("Enter your 2nd Number: "))
list = [10, 20, 30, 40]


total_sum = num1 + num2
print(f"Sum of {num1} + {num2} = {total_sum}")

defrent = num1 - num2
print(f"Difrent of {num1} + {num2} = {defrent}")

if num1 > num2:
    print("Bada number ka square =", num1 ** 2)
    print("Chhote number ka cube =", num2 ** 3)
elif num2 > num1:
    print("Bada number ka square =", num2 ** 2)
    print("Chhote number ka cube =", num1 ** 3)
else:
    print("Dono equal hain, isliye square aur cube alag se nahi nikala ja raha.")


if num1 == num2:
    print("equal")
else:
    print("Not equal")


if num1 in list:
    print("1st Number exist in list")
elif num2 in list:
    print("2nd Number exist in list")