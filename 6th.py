"""
first = (input("Enter first name: "))
second = (input("Enter second name: "))
print(first, second)
print(len(first))
"""

"""
str = "Hi, $Iam the $ symbol $ 99.99"
print(str.count("$"))
"""

#conditional operators
"""
light = "Blue"

if light == "Red":
    print("You can stop")
elif light == "Green":
    print("You can go")
elif light == "Yelow":
    print("You can slow down")
else:
    print("light is broken")    
"""

#grade student based on marks
"""
marks = 80
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")
"""

#check the number is even or odd user entered
"""
str = input("Enter a number: ")
num = int(str)
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
"""

#greatest of three numbers entered by user
"""
str = input("Enter first number: ")
num1 = int(str)
str = input("Enter second number: ")
num2 = int(str)
str = input("Enter third number: ")
num3 = int(str)
if num1 >= num2 and num1 >= num3:
    print("Greatest is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Greatest is:", num2)
else:
    print("Greatest is:", num3)
    """

#if the check multiple of 7 or not
str = input("Enter a number: ")
num = int(str)
if num % 7 == 0:
    print("Multiple of 7")
else:
    print("Not a multiple of 7")
    
    