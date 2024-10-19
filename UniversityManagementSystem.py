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

    def findStudentById(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def findTeacherById(self, teacher_id):
        for teacher in self.teachers:
            if teacher.teacher_id == teacher_id:
                return teacher
        return None

    def __str__(self):
        return (f"╔══════════════════════════════════════╗\n"
                f"║ University: {self.name}\n"
                f"║ Total Students: {len(self.students)}\n"
                f"║ Total Teachers: {len(self.teachers)}\n"
                f"║ Total Sections: {len(self.sections)}\n"
                f"╚══════════════════════════════════════╝")


def getInteger(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def getValidString(prompt):
    while True:
        value = input(prompt)
        if all(char.isalpha() or char.isspace() for char in value) and value.strip():
            return value
        else:
            print("Invalid input. Please enter a valid name (letters and spaces only).")


def main():
    university_name = getValidString("Enter the name of the university: ")
    uni = University(university_name)
    num_teachers = getInteger("Enter the number of teachers: ")
    for _ in range(num_teachers):
        print(f"\nEntering details for Teacher:")
        name = getValidString("Enter teacher name: ")
        age = getInteger("Enter teacher age: ")
        teacher_id = input("Enter teacher ID: ")
        teacher = Teacher(name, age, teacher_id)
        uni.addTeacher(teacher)
    num_students = getInteger("\nEnter the number of students: ")
    for _ in range(num_students):
        print(f"\nEntering details for Student:")
        name = getValidString("Enter student name: ")
        age = getInteger("Enter student age: ")
        student_id = input("Enter student ID: ")
        student = Student(name, age, student_id)
        uni.addStudent(student)
    num_sections = getInteger("\nEnter the number of sections: ")
    for _ in range(num_sections):
        print(f"\nEntering details for Section:")
        section_name = input("Enter section name: ")
        section = Section(section_name)
        teacher_id = input("Enter the teacher ID for this section: ")
        teacher = uni.findTeacherById(teacher_id)
        if teacher:
            section.assignTeacher(teacher)
        else:
            print(f"No teacher found with ID {teacher_id}")
        class_name = input("Enter course name and code: ")
        start_time = input("Enter class start time: ")
        end_time = input("Enter class end time: ")
        room_number = input("Enter room number: ")
        class_info = Class(class_name, start_time, end_time, room_number)
        section.setClassInfo(class_info)
        num_section_students = getInteger(
            "Enter the number of students in this section: ")
        for _ in range(num_section_students):
            print(f"Adding Student to Section:")
            student_id = input("Enter student ID: ")
            student = uni.findStudentById(student_id)
            if student:
                section.addStudent(student)
            else:
                print(f"No student found with ID {student_id}")
        uni.addSection(section)
    print("\nUniversity Summary:")
    print(uni)
    for section in uni.sections:
        print(section)


if __name__ == "__main__":
    main()
