#CGPA grading system
CGPA = float(input("Enter your CGPA: "))

if CGPA  >= 4.50 and  CGPA <= 5.0:
    grade = 'FIRST CLASS!'
elif CGPA >= 3.50 and CGPA <=4.49:
    grade = 'SECOND CLASS UPPER'
elif CGPA >= 2.50 and CGPA <=3.49:
    grade = 'SECOND CLASS LOWER'
elif CGPA >= 1.50 and CGPA <=2.49:
    grade = 'THIRD CLASS'
elif CGPA >= 0.00 and CGPA <= 1.49:
    grade = 'FAIL'
else:
    print(" input a valid grade between 0.0 - 5.0")

print(f"Your CGPA grade is: {grade}")
