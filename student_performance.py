student_name = input("Enter your name:")
no_subject = int(input("Enter no of subjects:"))
total = 0
for i in range(no_subject):
     mark = float(input(f"Mark of subject{i+1}:"))
     total += mark
percentage = total/no_subject
if percentage >=90:
     grade = "A+"
     performance = "outstanding"
elif percentage >=80:
     grade = "A"
     performance = "Excellent"
elif percentage >= 70:
     grade = "B"
     performance = "Very Good"
elif percentage >= 60:
     grade = "C"
     performance = "Good"
elif percentage >=50:
     grade = "D"
     performance = "Average"
else:
     grade = "F"
     performance = "Need Improvement"
print("Student Details")     
print("Name of the Student:",student_name)
print("Total marks:",total)
print("Percentage:",round(percentage,2),"%")
print("Grade:",grade)
print("Performance:",performance)

