# Student Management System (OOP Final Project)

A simple command-line Student Management System built in Python to practice core Object-Oriented Programming concepts: classes, encapsulation, `__str__`/`__repr__`, class-level attributes, and multi-file project structure.

The system lets you manage students and courses, enroll students in courses, record grades, and search/list records — all through an interactive terminal menu.

## Features

- Add / remove students
- Add / remove courses
- Enroll a student in a course (with duplicate-enrollment protection)
- Record a grade for a student in a course (with `0–100` validation)
- Search courses by name
- List all students / all courses
- Input validation with friendly error messages (invalid IDs, empty names, out-of-range grades, etc.)
- Auto-incrementing unique IDs for both students and courses

## Project Structure

```
OOP_Final_Course/
├── core/
│   ├── __init__.py
│   └── sysmanager.py     # SystemManager: central logic tying students & courses together
├── model/
│   ├── __init__.py
│   ├── student.py        # Student class
│   └── course.py         # Course class
├── main.py                # CLI entry point (menu-driven interface)
├── test.ipynb              # Notebook used for prototyping / testing classes
└── README.md
```

## Class Overview

### `Student` (`model/student.py`)
Represents a student with a unique auto-generated ID, name, grades, and enrolled courses.

| Method | Description |
|---|---|
| `__init__(name)` | Creates a student and assigns a unique `student_id` |
| `add_grade(course, grade)` | Records a grade for a given course |
| `enrolled_in_course(course)` | Adds a course to the student's enrolled list |
| `__str__()` | Human-readable summary of the student |

### `Course` (`model/course.py`)
Represents a course with a unique auto-generated ID, name, and list of enrolled students.

| Method | Description |
|---|---|
| `__init__(name)` | Creates a course and assigns a unique `course_id` |
| `enroll_student(student)` | Enrolls a student (prevents duplicates) |
| `remove_student(student)` | Removes a student from the course |
| `__str__` / `__repr__` | Human-readable summary of the course |

### `SystemManager` (`core/sysmanager.py`)
The central manager that owns all students and courses and coordinates operations between them.

| Method | Description |
|---|---|
| `add_student(name)` | Creates and registers a new student |
| `remove_student(student_id)` | Removes a student and unenrolls them from all courses |
| `add_course(name)` | Creates and registers a new course |
| `remove_course(course_id)` | Removes a course (blocked if students are still enrolled) |
| `enroll_course(student_id, course_id)` | Enrolls a student in a course |
| `record_grade(student_id, course_id, grade)` | Records a grade (validates `0 ≤ grade ≤ 100`) |
| `search_courses(search_name)` | Case-insensitive substring search on course names |
| `get_all_students()` / `get_all_courses()` | Returns all registered students / courses |

## Getting Started

### Prerequisites
- Python 3.10+ (uses `str | None` type hint syntax)

### Installation

```bash
git clone https://github.com/engysaber0/AI_Diploma.git
cd AI_Diploma/Tasks/OOP_Final_Course
```

### Running the Application

```bash
python main.py
```

You'll be presented with a menu:

```
==================================================
1. Add student
2. Remove student
3. Add course
4. Remove course
5. Search courses
6. Record grade
7. Get all students
8. Get all courses
9. Enroll course
10. Exit
==================================================
Enter choice:
```

Enter the number corresponding to the action you want to perform, and follow the prompts.

## Example Usage

```
Enter choice: 1
Enter student name: Engy
Student 'Engy' added successfully with ID 1.

Enter choice: 3
Enter course name: Machine Learning
Course 'Machine Learning' added successfully with ID 1.

Enter choice: 9
Enter student ID: 1
Enter course ID: 1
Student 'Engy' enrolled in course 'Machine Learning' successfully.

Enter choice: 6
Enter student ID: 1
Enter course ID: 1
Enter grade (0-100): 90
Grade 90.0 recorded for student 'Engy' in course 'Machine Learning'.
```

## Running Tests

Unit tests (using `unittest`) are included for the `Student` class in `test.ipynb`. To run them from a plain Python file, you can adapt the notebook cells into a `test_student.py` file and run:

```bash
python -m unittest test_student.py
```
