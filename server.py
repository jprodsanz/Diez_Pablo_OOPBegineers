# # Object Oriented Programming in Python
# # https://youtu.be/JeznW_7DlB0

class Student:
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade

# parameters give the fuctions what it needs in order to actually run the instructions
# . go inside class, indidcates it belongs to class
# objects are an instace of a class  

class Course:
    def __init__(self,name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0 
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1 = Student('Pablo',19, 95)
s2 = Student('Sara',17, 91)
s3 = Student('Sofia',22, 75)

course = Course("Science", 2,)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
print(course.get_average_grade())

