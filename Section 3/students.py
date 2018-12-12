
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    def average(self):
        return sum(self.marks) / (len(self.marks))

class WorkingStudent (Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def monthly_salary(self):
        return self.salary / 12


john = WorkingStudent('John', 'OSU', 60000)
print(john.salary)
john.marks.append(100)
john.marks.append(89)
print(john.average())
print(john.monthly_salary())