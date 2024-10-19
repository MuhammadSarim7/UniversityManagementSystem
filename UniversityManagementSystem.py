class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


class Teacher(Human):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id


class Class:
    def __init__(self, name, start_time, end_time, room_number):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.room_number = room_number

    def __str__(self):
        return (f"Class: {self.name}\n"
                f"Class Time: {self.start_time} - {self.end_time}\n"
                f"Room Number: {self.room_number}")


class Section:
    def __init__(self, name, teacher=None):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.class_info = None

    def assignTeacher(self, teacher):
        self.teacher = teacher

    def addStudent(self, student):
        self.students.append(student)

    def setClassInfo(self, class_info):
        self.class_info = class_info

    def __str__(self):
        student_names = [student.name for student in self.students]
        teacher_name = self.teacher.name if self.teacher else 'None'
        class_details = str(
            self.class_info) if self.class_info else "No class information"
        return (f"┌─────────────────────────────────────────┐\n"
                f"│ Section: {self.name}\n"
                f"│ Teacher: {teacher_name}\n"
                f"│ Students: {', '.join(student_names)
                               if student_names else 'None'}\n"
                f"│ Class Info:\n{class_details}\n"
                f"└─────────────────────────────────────────┘")


class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.sections = []

    def addStudent(self, student):
        self.students.append(student)

    def addTeacher(self, teacher):
        self.teachers.append(teacher)

    def addSection(self, section):
        self.sections.append(section)

    