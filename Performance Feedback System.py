print(" Performance Feedback System")

name = input("Enter your name: ")
roll_number= int(input("Enter your roll number:"))
course = input("Enter your Course Name: ")
maths = int(input("Enter marks of maths: "))
science = int(input("Enter marks of science : "))
english = int(input("Enter marks of english: "))

total = maths + science + english
percentage = total / 3

# Grade logic
if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'
else:
    grade = 'F'

# Output
print("\n--- Report Card ---")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2))
print("Grade:", grade)
print("\n Thank you for using My Performance Feedback System!")
