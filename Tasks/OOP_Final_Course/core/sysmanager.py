from model.student import Student
from model.course import Course
class SystemManager:
    def __init__(self):
        self.students = {}  
        self.courses = {} 

    def add_student(self, name):
        if not name.strip():
            print("Error: Student name cannot be empty.")
            return None
        student = Student(name)
        self.students[student.student_id] = student
        print(f"Student '{name}' added successfully with ID {student.student_id}.")
        return student.student_id

    def remove_student(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            # إزالة الطالب من كل الكورسات المسجل فيها
            for course in list(student.enrolled_courses):
                course.remove_student(student)
                student.enrolled_courses.remove(course)
            del self.students[student_id]
            print(f"Student '{student.name}' removed successfully.")
        else:
            print("Invalid student ID.")

    def add_course(self, name):
        if not name.strip():
            print("Error: Course name cannot be empty.")
            return None
        course = Course(name)
        self.courses[course.course_id] = course
        print(f"Course '{name}' added successfully with ID {course.course_id}.")
        return course.course_id

    def remove_course(self, course_id):
        if course_id in self.courses:
            course = self.courses[course_id]
            if course.enrolled_students:
                print("Course has enrolled students. Cannot remove.")
            else:
                del self.courses[course_id]
                print(f"Course '{course.name}' removed successfully.")
        else:
            print("Invalid course ID.")

    def enroll_course(self, student_id, course_id):
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            course = self.courses[course_id]
            if course not in student.enrolled_courses:
                student.enroll_in_course(course)
                course.enroll_student(student)
                print(f"Student '{student.name}' enrolled in course '{course.name}' successfully.")
            else:
                print(f"Student '{student.name}' is already enrolled in course '{course.name}'.")
        else:
            print("Invalid student or course ID.")

    def record_grade(self, student_id, course_id, grade):
        if student_id in self.students and course_id in self.courses:
            if not (0 <= grade <= 100):
                print("Error: Grade must be between 0 and 100.")
                return
            student = self.students[student_id]
            course = self.courses[course_id]
            if course in student.enrolled_courses:
                student.add_grade(course, grade)
                print(f"Grade {grade} recorded for student '{student.name}' in course '{course.name}'.")
            else:
                print(f"Student '{student.name}' is not enrolled in course '{course.name}'.")
        else:
            print("Invalid student or course ID.")

    def search_courses(self, search_name):
        result = []
        for course in self.courses.values():
            if search_name.lower() in course.name.lower():
                result.append(course)
        return result

    def get_all_students(self):
        return list(self.students.values())

    def get_all_courses(self):
        return list(self.courses.values())