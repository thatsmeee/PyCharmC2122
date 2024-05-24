class Person:
    name: str
    surname: str
    age: int
    pensione: bool

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.set_pensione(self.age)

    def set_pensione(self, value: int):
        if value >= 60:
            self.pensione = True
        else:
            self.pensione = False

    def info_person(self):
        print(f'person:\t{self.name} | {self.surname} | {self.age}')

class Teacher(Person):
    subject: str
    hours: int

    def __init__(self, subject: str, hours: int, name: str, surname: str, age: int):
        self.subject = subject
        self.hours = hours
        Person.__init__(self, name=name, surname=surname, age=age)

    def info_teacher(self):
        print(f'teacher: {self.subject} | {self.hours}')

    def info_all(self):
        self.info_person()
        self.info_teacher()

class Student(Person):
    progress: str
    group: int

    def __init__(self, progress: int, group: str, name: str, surname: str, age: int):
        self.progress = progress
        self.group = group
        self.set_pensione(age)
        Person.__init__(self, name=name, surname=surname, age=age)

    def info_student(self):
        print(f'student: {self.group} | {self.progress} | {self.pensione}')

    def info_all(self):
        self.info_person()
        self.info_student()

class Worker(Person):
    position: str
    duties: str

    def __init__(self, position: str, duties: str, name: str, surname: str, age: int):
        self.position = position
        self.duties = duties
        self.set_pensione(age)
        Person.__init__(self, name=name, surname=surname, age=age)

    def info_worker(self):
        print(f'worker: {self.position} | {self.duties} | {self.pensione}')

    def info_all(self):
        self.info_person()
        self.info_worker()

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

group_name = input("\nEnter group name: ")
age_range = input("Enter age range: ")
students = []
print("")
teacher = Teacher(subject='Pycharm', hours=24, name='Teacher', surname='Lehrerin', age=30)
teacher.info_all()
print("")
student_pensione = Person.set_pensione(Student, 14)
student = Student(progress='10', group='C2122', name='Student', surname='Schüler', age=14)
student.info_all()
students.append(student)
print("")
student_pensione = Person.set_pensione(Student, 16)
student2 = Student(progress='11', group='C2122', name='Studentin', surname='Schülerin', age=16)
student2.info_all()
students.append(student2)
print("")
worker_pensione = Person.set_pensione(Worker, 62)
worker = Worker(position='Boss', duties='Make business grow', name='Worker', surname='Arbeiter', age=62)
worker.info_all()
print("")
group = Group(group_name=group_name, students=students, age=age_range)
group.info_group()