# Student Course Management System

This Python-based system is designed to manage students, their courses, and grades. It supports functionalities such as adding and updating student information, listing all students and courses, and calculating average grades for a set of students.

## Features

- **Add and Update Students:** You can add new students with their respective courses and age, or update existing student details such as their age and courses.
- **List Students and Courses:** It allows you to list all students and all courses offered across students.
- **Average Grade Calculation:** It provides a function to calculate the average grade based on the grades provided.
- **Student Course Information:** You can retrieve the list of courses each student is enrolled in.

## Setup

1. Install Python (3.x recommended).
2. Copy the provided script into a Python file (e.g., `student_management.py`).
3. Run the script using any Python interpreter.

## Usage

### Example Code Snippet:

```python
# Add a new student
add_student('Eve', 24, ['Math', 'Physics'])

# Update an existing student
update_student('Ali', age=21)

# Calculate the average grade for a student
average = calc_average_grade([85, 90, 80])

# List all students
print("All students:", list_all_students())

# List all available courses
print("All courses:", list_all_courses())

# List courses of a specific student
print("Charlie's courses:", list_student_courses('Cha'))

# Print average grade
print(f"Alice's average grade: {average}")
```

### Functions:

1. **`add_student(name, age, courses)`**  
   Adds a new student to the system.

2. **`update_student(name, age=None, courses=None)`**  
   Updates the details of an existing student, including age and courses.

3. **`calc_average_grade(grades)`**  
   Calculates the average grade from a list of grades.

4. **`list_all_students()`**  
   Lists all the students in the system.

5. **`list_all_courses()`**  
   Lists all the courses across all students.

6. **`list_student_courses(name)`**  
   Lists all the courses a specific student is enrolled in.

### Data Structure:

- **Students**: A list of student names.
- **Courses**: A tuple of course names.
- **Student Info**: A dictionary where the key is the student's name, and the value is a dictionary containing the student's age and the list of courses they are enrolled in.
- **Grades**: A numpy array representing the grades for each student in different courses.

### Example Output:

```python
All students: ['Ali', 'Bob', 'Cha', 'Dinaa', 'Eve']
All courses: ['Computer Science', 'Math', 'Physics', 'History']
Charlie's courses: ['Math', 'History']
Alice's average grade: 85.0
```

### Displayed Data:

- **Students:** A list of students' names.
- **Courses:** A list of all available courses across students.
- **Student Info:** A dictionary containing each student's details including their age and enrolled courses.
- **Grades:** A 2D numpy array representing grades for each student in each course.

## Example Data:

```python
# Students Information:
{
    'Ali': {'age': 21, 'courses': ['Math', 'Computer Science']},
    'Bob': {'age': 22, 'courses': ['Physics', 'History']},
    'Cha': {'age': 21, 'courses': ['Math', 'History']},
    'Dinaa': {'age': 23, 'courses': ['Physics', 'Computer Science']},
    'Eve': {'age': 24, 'courses': ['Math', 'Physics']}
}

# Grades Array:
[[85  0 90  0]  
 [ 0 88  0 92]  
 [78  0  0 80]  
 [ 0 91 95  0]]
```

## Requirements

- Python 3.x
- Numpy library (`pip install numpy`)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
