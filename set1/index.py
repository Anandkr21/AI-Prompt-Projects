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



# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
    # - *Input*: None
    # - *Output*: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20

#list of number
number = [1,2,3,4,5,6,7,8,9,10]
print(number)

# add a number
number.append(20)
print(number)

# remove
number.remove(3)
print(number)

# sort the list
randomNumber = [2,4,1,5,32,3,7]
randomNumber.sort()
print(randomNumber)


# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"


num = [10, 20, 30, 40]

total_sum = sum(num)
print(total_sum)

# avg of all num
avg = total_sum/len(num)
print(avg)


# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"

def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string


input_string = "Python"
reversed_string = reverse_string(input_string)
print(reversed_string)



# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"

def countVowel(inputString):
    vowels = "aeiouAEIOU"
    count = 0

    for char in inputString:
        if char in vowels:
            count += 1

    return count

# Example usage
inputString = "Hello!"
vowelCount = countVowel(inputString)
print("Number of vowels:", vowelCount)


# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


number = 13
is_prime_number = is_prime(number)
print(f"{number} is prime: {is_prime_number}")



# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
number = 5
factorial_result = factorial(number)
print(f"The factorial of {number} is: {factorial_result}")


# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"

def fibonacci(n):
    if n <= 0:
        return []

    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence[:n]

n = 10
fibonacci_sequence = fibonacci(n)
print(f"The first {n} numbers in the Fibonacci sequence are: {fibonacci_sequence}")


# 10. **List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1  to 10.
#     - *Input*: None
#     - *Output*: "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"
squares = [x ** 2 for x in range(1, 11)]
print(squares)
