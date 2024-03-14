class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привіт, мене звати {self.name}, мені {self.age} років.")


class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def work(self):
        print(f"{self.name} працює на посаді {self.position}.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} займається навчанням, його студентський ID: {self.student_id}.")


class University:
    def __init__(self):
        self.employees = []
        self.students = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_student(self, student):
        self.students.append(student)

    def remove_employee(self, name):
        self.employees = [emp for emp in self.employees if emp.name != name]

    def remove_student(self, student_id):
        self.students = [stu for stu in self.students if stu.student_id != student_id]

    def find_person(self, identifier):
        for person in self.employees + self.students:
            if person.name == identifier or getattr(person, 'student_id', None) == identifier:
                print(f"Знайдено: {person.name}, Вік: {person.age}")
                return person
        print("Нічого не знайдено.")
        return None

    def show_info(self):
        print("Інформація про університет:")
        for employee in self.employees:
            employee.introduce()
            employee.work()
        for student in self.students:
            student.introduce()
            student.study()


employee = Employee("Андрій", 30, "викладач")
student = Student("Олена", 20, "S123456")

university = University()
university.add_employee(employee)
university.add_student(student)

university.show_info()

university.find_person("Андрій")
university.find_person("S123456")

university.remove_employee("Андрій")
university.remove_student("S123456")

university.show_info()
