import numpy as np


students = ['Ali', 'Bob', 'Cha', 'Dinaa']


courses = ('Math', 'Physics', 'Computer Science', 'History')


students_info = {
    'Ali': {'age': 20, 'courses': ['Math', 'Computer Science']},
    'Bob': {'age': 22, 'courses': ['Physics', 'History']},
    'Cha': {'age': 21, 'courses': ['Math', 'History']},
    'Diinaa': {'age': 23, 'courses': ['Physics', 'Computer Science']}
}

grades = np.array([
    [85, 0, 90, 0],  
    [0, 88, 0, 92],  
    [78, 0, 0, 80],  
    [0, 91, 95, 0]   
])


def add_student(name, age, courses):
    students_info[name] = {'age': age, 'courses': courses}

def update_student(name, age=None, courses=None):
    if age is not None:
        students_info[name]['age'] = age
    if courses is not None:
        students_info[name]['courses'] = courses


def calc_average_grade(grades):
    return sum(grades) / len(grades)


def list_all_students():
    return list(students_info.keys())


def list_all_courses():
    courses = []
    for student in students_info.values():
        courses.extend(student['courses'])
    return list(set(courses))  

def list_student_courses(name):
    return students_info[name]['courses']



add_student('Eve', 24, ['Math', 'Physics'])
update_student('Ali', age=21)
average = calc_average_grade([85, 90, 80])  


print("All students:", list_all_students())
print("All courses:", list_all_courses())
print("Charlie's courses:", list_student_courses('Cha'))
print(f"Alice's average grade: {average}")



# display the data of students, courses, students_info, and grades


































# Display the data
print("Students:", students)
print("Courses:", courses)
print("Student Info:", students_info)
print("Grades array:\n", grades)
