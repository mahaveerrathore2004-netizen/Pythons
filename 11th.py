#loops in python
"""
count = 1
while count <= 5:
    print("Hello World")
    count += 1

i = 1
while i <= 10:
    print("Rajasthan", i)
    i += 1    

i = 1
while i <= 10:
    print(i)
    i += 1

i = 10
while i >= 1:
    print(i)
    i -= 1
    
print("Done")    
"""
"""
i = 1
while i <= 100:
    print(i)
    i += 1

i = 100
while i >= 1:
    print(i)
    i -= 1
"""
"""
n = int(input("Enter a number :"))
i = 1
while i <= 10:
    print(n * i)
    i += 1

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1    
"""
"""
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36]

x = 36

i = 0
while i < len(nums):
    if nums[i] == x:
        print("FOUND at idx", i)
    i += 1
"""

#break & continue statement

i = 1
while i <= 10:
    print(i)
    if i == 7:
        break
    i += 1
print("Done")

i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
print("Done")