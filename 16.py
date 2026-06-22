"""
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Python", "Java")
print(new_data)    

with open("practice.txt", "w") as f:
    f.write(new_data)
"""
"""
def check_for_word():
    word = "programming"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(word in data):
            print("Found")
        else:
            print("not found")  

check_for_word()


def check_for_line():
    word = "programming"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1
check_for_line()        
"""

with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if data[i] == ",":
            print(num)
            num = ""
        else:
            num += data[i]

    if num:
        print(num)
