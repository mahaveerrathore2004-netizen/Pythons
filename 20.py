
"""
class Person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name

p1 = Person()
p1.changeName("KIrtik")        
print(p1.name)
print(Person.name)
"""
"""
class Person:
    name = "anonymous"

    def changeName(self, name):
        Person.name = name

p1 = Person()
p1.changeName("KIrtik")        
print(p1.name)
print(Person.name)
"""
"""
class Person:
    name = "anonymous"

    def changeName(self, name):
        self.__class__.name = "Kirtik"

p1 = Person()
p1.changeName("KIrtik")        
print(p1.name)
print(Person.name)
"""

#class method
"""
class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Kirtik")
print(p1.name)
print(Person.name)        
"""

#property
"""
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) /3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)
"""

#polymorphism
"""
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
    
    def __mul__(self, num2):
        newReal = self.real * num2.real
        newImg = self.img * num2.img
        return Complex(newReal, newImg)
    
    def __truediv__(self, num2):
        newReal = self.real / num2.real
        newImg = self.img / num2.img
        return Complex(newReal, newImg)
    
    def __mod__(self, num2):
        newReal = self.real % num2.real
        newImg = self.img % num2.img
        return Complex(newReal, newImg)
    
num1 = Complex(1, 3)
num1.showNumber()  

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num3 = num1 - num2
num3.showNumber()

num3 = num1 * num2
num3.showNumber()

num3 = num1 / num2
num3.showNumber()

num3 = num1 / num2
num3.showNumber()
"""

#practice questions
"""
class Circle:
    def __init__(self, redius):
        self.reduis = redius

    def area(self):
        return 3.14 * self.reduis ** 2

    def perimeter(self):
        return 2 * 3.14 * self.reduis

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())
"""

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "95,000")


eng1 = Engineer("Kirtik", 21)
eng1.showDetails()
