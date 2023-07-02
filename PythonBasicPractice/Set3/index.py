# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
#     - *Input*: [("John", 25), ("Jane", 30)]
#     - *Output*: "John is 25 years old. Jane is 30 years old."

people = [("John", 25), ("Jane", 30)]

for name, age in people:
    print(f"{name} is {age} years old.")


# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"
def add_name_age(dictionary, name, age):
    dictionary[name] = age
    return dictionary

def update_age(dictionary, name, age):
    if name in dictionary:
        dictionary[name] = age
        return dictionary
    else:
        return "Name not found in the dictionary."

def delete_name(dictionary, name):
    if name in dictionary:
        del dictionary[name]
        return dictionary
    else:
        return "Name not found in the dictionary."

# Create an empty dictionary
my_dictionary = {}

# Add a new name-age pair
my_dictionary = add_name_age(my_dictionary, "John", 25)
print(my_dictionary)

# Update the age of a name
my_dictionary = update_age(my_dictionary, "John", 26)
print(my_dictionary)

# Delete a name from the dictionary
my_dictionary = delete_name(my_dictionary, "John")
print(my_dictionary)

# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"
def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []

nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print(result)



#**Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."

def is_palindrome(word):
    # Remove any whitespace and convert to lowercase
    word = word.replace(" ", "").lower()
    # Check if the word is equal to its reverse
    if word == word[::-1]:
        return True
    else:
        return False

input_word = "madam"

if is_palindrome(input_word):
    print("The word", input_word, "is a palindrome.")
else:
    print("The word", input_word, "is not a palindrome.")


#**Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

input_arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(input_arr)
print(sorted_arr)


#Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"
from queue import Queue

class Stack:
    def __init__(self):
        self.queue = Queue()

    def push(self, item):
        self.queue.put(item)

    def pop(self):
        if self.queue.empty():
            return None
        # Move all items except the last one to a temporary queue
        temp_queue = Queue()
        while self.queue.qsize() > 1:
            temp_queue.put(self.queue.get())
        # Remove and return the last item from the original queue
        popped_item = self.queue.get()
        # Put back the items from the temporary queue to the original queue
        while not temp_queue.empty():
            self.queue.put(temp_queue.get())
        return popped_item

stack = Stack()

stack.push(1)
stack.push(2)
print(stack.pop())
stack.push(3)
print(stack.pop())
print(stack.pop())


# 1. **FizzBuzz**: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
#     - *Input*: None
#     - *Output*: "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16,..."
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)



#File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"







#**Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

num1 = 5
num2 = 0
division_result = divide_numbers(num1, num2)
print(division_result)

