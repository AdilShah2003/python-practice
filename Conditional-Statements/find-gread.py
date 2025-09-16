# hindi = 0, english = 0, math = 0, py = 0, chem = 0
marks = [0, 0, 0, 0, 0] 
subject = ["Hindi", "English", "Math", "py", "Chem"]

print(type(subject))

for i in range(len(subject)):
    marks[i] = int(input(f"Enter your {subject[i]} Marks: "))
    
print(marks)

total = sum(marks)
print(total)

avg = total / len(marks)
print(avg)

if avg > 90:
    print("Grade A")
elif avg >= 75 and avg < 90:
    print("Grade B")
elif avg >= 50 and avg <  74:
    print("Grade C")
elif avg < 50:
    print("Fail")
