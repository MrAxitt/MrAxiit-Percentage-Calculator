# Intro
input("Welcome to Percentage Calculator!")
input("Please provide all the details as asked—this program will use them to calculate your percentage and final grade.")
# Data Collection
no_of_subjects = int(input("How many subjects are you currently studying?"))
subjects = input("Please list all the subjects you are currently studying (separated by commas)")
subject_list = subjects.split(",")
mark_obtained = []
for subjects in subject_list:
    mark = int(input(f"Enter the marks obtained in {subjects.strip()}:"))
    mark_obtained.append(mark)
total_marks = int(input("What are the total marks for each subject? (assuming same for all)"))
# Percentage Calculation
total_marks_obtained = sum(mark_obtained)
total_marks_possible = no_of_subjects * total_marks
percentage = total_marks_obtained / total_marks_possible * 100
# Grade Determination
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = ("B")
elif percentage >= 60:
    grade = ("C")
elif percentage >= 50:
    grade = ("D")
else:
    grade = ("F")
# Data Display
print("---MARKS BREAKDOWN---")
for i in range(no_of_subjects):
    print(f"{subject_list[i].strip()} = {mark_obtained[i]} / {total_marks}")
print(f"Percentage: {percentage}")
print(f"Grade: {grade}")
