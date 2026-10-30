
print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))
mark4 = float(input("Enter mark for Subject 4: "))
mark5 = float(input("Enter mark for Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5

print("\n===== STUDENT REPORT =====")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)

if any(mark < 0 or mark > 100 for mark in [mark1, mark2, mark3, mark4, mark5]):
    print("Invalid marks entered!")

elif any(mark < 35 for mark in [mark1, mark2, mark3, mark4, mark5]):
    print("Result: FAIL")
    print("Grade: F")

else:
    print("Result: PASS")

    if average >= 90:
        print("Grade: A+")
    elif average >= 80:
        print("Grade: A")
    elif average >= 70:
        print("Grade: B")
    elif average >= 60:
        print("Grade: C")
    else:
        print("Grade: D")
