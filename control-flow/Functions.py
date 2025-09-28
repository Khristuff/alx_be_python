def calculate_area(lenght, width):
    area = lenght * width
    return area
calculate_area(5, 10)
#print(calculate_area(5, 10))  # Output: 50

"""def greet(name):
    return f"Hello, {name}!"
print(greet("Chris"))
print(greet("Anna"))
print(greet("Nkem"))
print(greet("Vickie"))
"""

def user_info(name, age=None):
    print(f"Name: {name}")
    if age:
        print(f"Age: {age}")

user_info(name="Chris", age=29)

def square(number):
    return number * number
squared_value = square(4)
print(squared_value)

x = "3.5"
print(int(float(x)) + 2)

import math
