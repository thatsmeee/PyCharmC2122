class StudySubject:
    def __init__(self, name: str, hours: int, enable: bool):
        self.name = name
        self.hours = hours
        self.enable = enable

    def info_study(self):
        print(f'Study: {self.name} | {self.hours} hour(s) | Studies it now: {self.enable}')

class Student:
    def __init__(self, name: str, surname: str, studies: list):
        self.name = name
        self.surname = surname
        self.studies = studies

    def info_student(self):
        print(f'Student: {self.name} {self.surname}')

    def info_all(self):
        self.info_student()
        for study in self.studies:
            study.info_study()

class Group:
    def __init__(self, group_name: str, students: list, age: str):
        self.group_name = group_name
        self.students = students
        self.age = age
        self.num_students = len(students)

    def info_group(self):
        print(f'Group: {self.group_name} | Number of Students: {self.num_students} | Age Range: {self.age}\n')
        for student in self.students:
            student.info_all()

subjects = []

def create_subject():
    subject_name = input("Enter subject name: ")
    subject_hours = int(input("Enter number of hours: "))
    subject_enable = input("Is subject enabled? (True/False): ").lower() == 'true'
    subjects.append(StudySubject(name=subject_name, hours=subject_hours, enable=subject_enable))

def create_student():
    student_name = input("Enter student name: ")
    student_surname = input("Enter student surname: ")
    student_studies = subjects.copy()
    students.append(Student(name=student_name, surname=student_surname, studies=student_studies))

num_subjects = int(input("\nEnter the number of subjects: "))
for _ in range(num_subjects):
    create_subject()

num_students = int(input("\nEnter the number of students: "))
students = []
for _ in range(num_students):
    create_student()

group_name = input("\nEnter group name: ")
age_range = input("Enter age range: ")
group = Group(group_name=group_name, students=students, age=age_range)

print("")
group.info_group()
