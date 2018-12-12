
def average_grade(student):
    return sum(student['grades']) / len(student['grades'])


# Objects stores data and action to happen to that data

class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grades = new_grade

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Jim Smith', [70, 82, 90, 77, 94])

print(student_one.name)
print(student_one.average())

def average(student):
    return sum(student.grades) / len(student.grades)

print(student_one.average())

class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director
    def print_movie(self):
        print('<<{}>>  by {}.'.format(self.name, self.director))
    # let's try to add a method `print_info()` here:

movie_one = Movie('The Big Lebowski', 'Cohen Brothers')