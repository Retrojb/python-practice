
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
# print(john.salary)
john.marks.append(100)
john.marks.append(89)
# print(john.average())
# print(john.monthly_salary())

bob = Student('Bob', 'OU')

## Instance: Takes object as the first arguement
## Class: takes class as first arguement
## nothing: takes nothing

class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)
my_object = Foo()
my_object.hi()

class Bar:
    @staticmethod
    def buzz():
        print('I dont take parameters')
second_object = Bar()
second_object.buzz()