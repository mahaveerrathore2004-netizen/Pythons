#for loop
"""
nums = [1, 2, 3, 4, 5]
for val in nums:
    print(val)


tup = (10, 20, 30, 40, 50)
for num in tup:
    print(num)
"""

"""
str = "mahaveerrathore"
for char in str:
    if(char == 'm'):
        print("o found")
        break
    print(char)
else:
    print("Done")
"""

#nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#for val in nums:
#    print(val)
"""
nums = {1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49}
x = 49

idx = 0
for el in nums:
    if(el == x):
        print("number found at idx", idx)
    idx += 1
"""

#range() function

#seq = range(10)
#for i in seq:
#    print(i)

#for i in range(2, 100, 2):
#    print(i)

"""
for i in range(1, 101):
    print(i)

for i in range(100, 0, -1):
    print(i)    
"""
"""
n = int(input("Enter a number :"))

for i in range(1, 11):
    print(n * i)
"""

#pass statement
"""
for i in range(1, 100):
    pass

if i % 2 == 0:
    pass
print("Done")
"""
"""
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("Sum is :", sum)   
"""

n = 5
fact = 1
i = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial is :", fact)