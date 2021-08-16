class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.is_active = False
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

s1 = Student('Alisson', 24, 95)
s2 = Student('Jhon', 18, 86)
s3 = Student('Carlos', 26, 80) 

course = Course('ADS', 2)
course.add_student(s1)
course.add_student(s2)

print(course.students)
      