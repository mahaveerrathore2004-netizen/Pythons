#OOP
#class & objects
"""
class Student:
    name = "Rohit"

s1 = Student()
print(s1.name) 
"""
"""
class Car:
    color1 = "blue"
    color2 = "black"
    brand1 = "mercedes"
    brand2 = "bmw"

car1 = Car()
print(car1.color1)
print(car1.brand1)

print(car1.color2)
print(car1.brand2)
"""

#__init__ function
"""
class Student:

    #default constructors
    def __init__(self):
        pass

    #parameterized constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")

s1 = Student("Kirtik", 98)       
print(s1.name, s1.marks)

s2 = Student("Yuvraj", 97)
print(s2.name, s2.marks)
"""

#class & instance attributes
"""
class Student:
    colage_name = "ABC Collage"
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")

s1 = Student("Kirtik", 98)       
print(s1.name, s1.marks)
"""

#Methods
"""
class Student:
    collage_name = "ABC Collage"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def welcome(self):
        print("welcome student", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Kirtik", 98)       
s1.welcome()
print(s1.get_marks())
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)

s1 = Student("Kirtik", [99, 98, 97])       
print(s1.name, s1.marks)
s1.get_avg()

