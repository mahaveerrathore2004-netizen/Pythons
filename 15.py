#file I/O 

#read
"""
f = open("demo.txt", "rt")

#data = f.read()
#print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()
"""

#write
"""
f = open("demo.txt", "w")

f.write("I want to learn Javascript tomorrow. 123")

f.close()
"""
"""
f = open("demo.txt", "a")
f.write("Then I'll move to Reactjs")
f.close()"""
"""
f = open("sample.txt", "w")
f.close()
"""
"""
f = open("demo.txt", "a+")
#f.write("abc")
print(f.read())
f.write("abc")

f.close()
"""
"""
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

with open("demo.txt", "w") as f:
    f.write("new data")    
    """

import os
os.remove("sample.txt")