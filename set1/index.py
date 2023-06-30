# 1. **Hello, World!**: Write a Python program that prints "Hello, World!" to the console.
#     - *Input*: None
#     - *Output*: "Hello, World!"

print('Namste World!')


# ---------------------------------------------------------------------

# 2. **Data Type Play**: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
#     - *Input*: None
#     - *Output*: "Type of variable1: <class 'int'>, value: 10..."

#integer
integer= 10;
print(f"Type of integer_var: {type(integer)}, value: {integer}")


#float
float= 3.144
print(f"Type of float_var: {type(float)}, value: {float}")


#String
string = 'anand'
print(f"Type of string: {type(string)}, value: {string}")

# Boolean
boolean = True;
print(f"Type of boolean {type(boolean)} , value: {boolean}")


# list
list_value = [ 1,2,3,4,5,6]
print(f'Type of list {type(list_value)}, value: {list_value}')


#tuple
tuple_list = (1,2,3,4,5)
print(f'Type of tupe are {type(tuple_list)}, value: {tuple_list}')


#dictionary
dictionary_list = {'name': 'Anand', 'age': 25, 'city': 'Patna'}
print(f'Type of dictionary {type(dictionary_list)}, value: {dictionary_list}')


#set
set_value = {1,5,2,6,4}
print(f'Type of set_value: {type(set_value)}, value: {set_value}')