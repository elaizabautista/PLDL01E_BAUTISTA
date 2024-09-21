#initialize final grade
final_grade=0

#input student name, midterm grade, minor b, final exam rating
student_name = input("Enter the student name;")
final_quizzes = float(input("Enter the final quizzes;"))
final_research_assignment = float(input("Enter the research/assignment rating;"))
final_project = float(input("Enter the final project;"))
final_exam = float(input("Enter the final exam;"))

#compute for final grade
final_grade = (0.30 * final_quizzes) + (0.10 * final_research_assignment) + (0.40 * final_exam) + (0.20 * final_project)

#determine equivalent grade based on final grade
def get_grade_remark(final_grade):
    if 98 <= final_grade <= 100:
        return 4.00
    elif 95 <= final_grade <= 97:
        return 3.75
    elif 92 <= final_grade <= 94:
        return 3.50
    elif 89 <= final_grade <= 91:
        return 3.25
    elif 86 <= final_grade <= 88:
        return 3.00
    elif 83 <= final_grade <= 85:
        return 2.75
    elif 80 <= final_grade <= 82:
        return 2.50
    elif 77 <= final_grade <= 79:
        return 2.25
    elif 74 <= final_grade <= 76:
        return 2.00
    elif 71 <= final_grade <= 73:
        return 1.75
    elif 68 <= final_grade <= 70:
        return 1.50
    elif 64 <= final_grade <= 67:
        return 1.25
    elif 60 <= final_grade <= 63:
        return 1.00
    else:
        return 0.00

#Output final grade and student details
print("Student Name:", student_name)
print("final quizzes:", final_quizzes)
print("final research/assignment:", final_research_assignment)
print("final project:", final_project)
print("final exam:", final_exam)
print("Equivalent Grade Remark:", get_grade_remark(final_grade))
