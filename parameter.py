
#by Peter
def pass_by_value(num):
    num += 10
    print("Inside pass_by_value:", num)

def pass_by_variable(lst):
    lst.append(4)
    print("Inside pass_by_variable:", lst)

def pass_by_reference(obj):
    obj["name"] = "John"
    print("Inside pass_by_reference:", obj)

# Example usage
x = 5
print("Before pass_by_value:", x)
pass_by_value(x)
print("After pass_by_value:", x)
print()

my_list = [1, 2, 3]
print("Before pass_by_variable:", my_list)
pass_by_variable(my_list)
print("After pass_by_variable:", my_list)
print()

my_dict = {"name": "Alice"}
print("Before pass_by_reference:", my_dict)
pass_by_reference(my_dict)
print("After pass_by_reference:", my_dict)

"""
#By Ian
#Passing by value
name = "ian"

def greet(name):
    print(f"Hello, {name}!")
greet(name)

#Passing by reference

def modify_list(lst):
    lst.append(4)
    lst[0] = 100

my_list = [1, 2, 3]
print("Before:", my_list)
modify_list(my_list)
print("After:", my_list)

#passing by variable

def multiply_numbers(a, b):
    result = a * b
    print(f"The product of {a} and {b} is: {result}")

# Variables
x = 5
y = 3

# Function call with variables as arguments
multiply_numbers(x, y)
"""


#NOTES
"""


"""