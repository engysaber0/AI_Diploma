class Course:
    _id_counter = 1

    def __init__(self, name):
        self.course_id = Course._id_counter
        Course._id_counter += 1
        self.name = name
        self.enrolled_students = []

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Enrolled Students: {self.enrolled_students}"

    def __repr__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Enrolled Students: {self.enrolled_students}"

    def enroll_student(self, student_name: str | None = "test") -> None:
        '''
        This function enrolls a student in the course. It takes the student's name as an argument and
        adds it to the list of enrolled students for this course.

        Args:
            student_name (str): The name of the student to enroll. Defaults to "test".
        Returns:
            None
        Example:
            c1 = Course("Mathematics")
            c1.enroll_student("George")
        '''
        if student_name not in self.enrolled_students:
            self.enrolled_students.append(student_name)
            print(f"Student {student_name} has been enrolled in {self.name}.")
        else:
            print(f"Student {student_name} is already enrolled in {self.name}.")

    def remove_student(self, student_name: str | None = "test") -> None:
        if student_name in self.enrolled_students:
            self.enrolled_students.remove(student_name)
            print(f"Student {student_name} has been removed from {self.name}.")