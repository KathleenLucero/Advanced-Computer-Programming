english = int(input("Enter grade for English: "))
filipino = int(input("Enter grade for Filipino: "))
science = int(input("Enter grade for Science: "))
math = int(input("Enter grade for Math: "))
araling_panlipunan = int(input("Enter grade for Araling Panlipunan: "))
physical_education = int(input("Enter grade for Physical Education: "))

num_grades = 6
sum_grades = english + filipino + science + math + araling_panlipunan + physical_education
avg_grade = sum_grades / num_grades

print("The average grade is:", avg_grade)