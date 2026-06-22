#recursive function
"""
def show(n):
    if(n == 0):
        return
    print(n)
    show(n - 1)
    print("END")
show(5)    
"""
"""
def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n - 1) * n
print(fact(2))
print(fact(3))
print(fact(4))
print(fact(5))
print(fact(6))
"""

#write a recursive function to calculate the sum of first n natural numbers
"""
def sum(n):
    if(n == 0):
        return 0
    return sum(n - 1) + n

print(sum(5))    
"""

#write a recursive function to print all elements in a list.
#hint : use list & index as parameters.

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "aople", "banana", "litchi"]

print_list(fruits)

