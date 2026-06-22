#function in python
"""
def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum

calc_sum(10, 20)
calc_sum(2.5, 4.5)
calc_sum(22, 33)
calc_sum(-5, 15)
calc_sum(1000, 2500)
"""

#average of 3 numbers in function
"""
def avg(a, b, c):
    sum = a + b + c
    average = sum / 3
    return average
print(avg(98, 97, 95))
"""

#default parameters
"""
def calc_prod(a=1, b=1):
    print(a * b)
    return a * b
calc_prod()

def calc_prod(a, b=20):
    print(a * b)
    return a * b
calc_prod(1)
"""
"""
cities = ["Jaipur", "Delhi", "Mumbai", "Bangalore"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)
"""
"""
cities = ["Jaipur", "Delhi", "Mumbai", "Bangalore"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item , end=" ")

print_list(heroes)
print_list(cities)
"""

"""
def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

fact(5)
fact(7)
fact(10)    
"""
"""
def convertor(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

convertor(25)
convertor(100)    
"""

#user define number of funtion odd and even numbers 
def odd_even(n):
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")
odd_even(10)
odd_even(7)
odd_even(0) 
odd_even(-3)