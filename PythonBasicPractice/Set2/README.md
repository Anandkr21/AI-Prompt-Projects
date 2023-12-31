# S1 D3 Assignment - Set 2

### Problem **1: Print the following pattern**

Write a program to print the following number pattern using a loop.

```python
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

### Problem **2: Display numbers from a list using loop**

Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

- The number must be divisible by five
- If the number is greater than 150, then skip it and move to the next number
- If the number is greater than 500, then stop the loop

**Given**:

```python
numbers = [12, 75, 150, 180, 145, 525, 50]
```

**Expected output:**

```python
75
150
145
```

### Problem **3: Append new string in the middle of a given string**

Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

**Given**:

```python
s1 = "Ault"
s2 = "Kelly"
```

**Expected Output**:

```python
AuKellylt
```

### Problem **4: Arrange string characters such that lowercase letters should come first**

Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

**Given**:

```python
str1 = PyNaTive
```

**Expected Output**:

```python
yaivePNT
```

### Problem **5: Concatenate two lists index-wise**

Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

**Given**:

```python
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
```

**Expected output:**

```python
['My', 'name', 'is', 'Kelly']
```

### Problem **6: Concatenate two lists in the following order**

```python
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
```

**Expected output:**

```python
['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
```

### Problem **7: Iterate both lists simultaneously**

Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

**Given**

```python
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
```

**Expected output:**

```python
10 400
20 300
30 200
40 100
```

### Problem **8: Initialize dictionary with default values**

In Python, we can initialize the keys with the same values.

**Given**:

```python
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
```

**Expected output:**

```python
{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
```

### Problem **9: Create a dictionary by extracting the keys from a given dictionary**

Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

**Given dictionary**:

```python
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
```

**Expected output:**

```python
{'name': 'Kelly', 'salary': 8000}
```

### Problem **10: Modify the tuple**

Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

**Given**:

```python
tuple1 = (11, [22, 33], 44, 55)
```

**Expected output:**