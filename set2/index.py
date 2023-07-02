# Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

row=5
for i in range(1, row+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

### Problem **2: Display numbers from a list using loop**

# Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

# **Given**:
# numbers = [12, 75, 150, 180, 145, 525, 50]

# **Expected output:**
# 75
# 150
# 145

numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
    if number > 500:
        break
    if number>150:
        continue
    if number%5==0:
        print(number)

### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

# **Given**:
# s1 = "Ault"
# s2 = "Kelly"

# **Expected Output**: ```
# AuKellylt

s1 = "Ault"
s2 = "Kelly"

middle_index = len(s1) // 2
s3 = s1[:middle_index] + s2 + s1[middle_index:]

print(s3)



### **Arrange string characters such that lowercase letters should come first**
# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# **Given**:
# str1 = PyNaTive
# **Expected Output**:  yaivePNT

str1 = "PyNaTive"

lowercase_letters = ""
uppercase_letters = ""

for char in str1:
    if char.islower():
        lowercase_letters += char
    else:
        uppercase_letters += char

arranged_str = lowercase_letters + uppercase_letters

print(arranged_str)


# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
# Given
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# Expected output:
# ['My', 'name', 'is', 'Kelly']

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

new_list = []

length = max(len(list1), len(list2))

for i in range(length):
    if i < len(list1) and i < len(list2):
        new_list.append(list1[i] + list2[i])
    elif i < len(list1):
        new_list.append(list1[i])
    else:
        new_list.append(list2[i])

print(new_list)



### Problem **6: Concatenate two lists in the following order**
# Given
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# **Expected output:**
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

concatenated_list = []

for word1 in list1:
    for word2 in list2:
        concatenated_list.append(word1 + word2)

print(concatenated_list)



### Problem **7: Iterate both lists simultaneously**
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
# **Given**
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# **Expected output:**
# 10 400
# 20 300
# 30 200
# 40 100
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

list2_reversed = list2[::-1]

for item1, item2 in zip(list1, list2_reversed):
    print(item1, item2)


### Problem **8: Initialize dictionary with default values**
# In Python, we can initialize the keys with the same values.
# **Given**:
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# **Expected output:**
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

result = {employee: defaults for employee in employees}

print(result)



### Problem **9: Create a dictionary by extracting the keys from a given dictionary**

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
# **Given dictionary**:
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# # Keys to extract
# keys = ["name", "salary"]
# **Expected output:**
# {'name': 'Kelly', 'salary': 8000}
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]

new_dict = {key: sample_dict[key] for key in keys}

print(new_dict)


### Problem **10: Modify the tuple**
# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222
# **Given**:
# tuple1 = (11, [22, 33], 44, 55)
# **Expected output:**
# tuple1: (11, [222, 33], 44, 55)
tuple1 = (11, [22, 33], 44, 55)

modified_list = list(tuple1)  # Convert the tuple to a list
modified_list[1][0] = 222  # Modify the first item of the list

tuple1 = tuple(modified_list)  # Convert the modified list back to a tuple

print("tuple1:", tuple1)
