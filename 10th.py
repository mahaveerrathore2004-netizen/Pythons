#store a following word meaning in a python dictionary
"""
table: " a piece of furniture ", "list of fatcs and figure "
cat: " a small animal "
"""
"""
word_meaning = {
    
    "cat": " a small animal ",
    "table": [" a piece of furniture" , "list of fatcs and figure "]
}
print(word_meaning)
print(word_meaning["table"])
print(word_meaning["cat"])  
"""

"""
subjects = {
    "python", "java", "c++", "python", "javascript", "java",
    "python", "java", "c++", "c"
}
print(subjects)
print(len(subjects))
"""

"""
marks = {}

x = int(input("Enter the number phy :"))
marks.update({"phy": x})

y = int(input("Enter the number chem :"))
marks.update({"chem": y})

z = int(input("Enter the number math :"))
marks.update({"math": z})

print(marks)
"""

value1 = {9, "9.0"}
print(value1)

value2 = {
    ("float", 9.0),
    ("int", 9)
}
print(value2)
