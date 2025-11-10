# conditionals.py
# Demonstrates if, elif, else statements

marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "C"

print("Marks:", marks)
print("Grade:", grade)
