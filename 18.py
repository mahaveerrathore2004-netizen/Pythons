#static method
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        total = 0
        for val in self.marks:
            total += val
        print("hi", self.name, "your avg score is:", total/len(self.marks))


s1 = Student("Kirtik", [99, 98, 97])

Student.hello()     
print(s1.name, s1.marks)
s1.get_avg()
"""

#abstraction
"""
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = Car()
car1.start()            
"""

#practice question
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    #credit method  
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance          

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)   
acc1.credit(50000)     
acc1.debit(10000)
