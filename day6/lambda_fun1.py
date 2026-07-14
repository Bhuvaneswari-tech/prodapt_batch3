'''
Problem Statement - Filter and Square Even Numbers
Write a Python program to filter all even numbers from a list and then find the square 
of each even number using lambda functions.

Requirements
Accept a list of integers from the user.
Use filter() with a lambda function to select only the even numbers.
Use map() with a lambda function to calculate the square of each even number.
Display the final list.
'''

#Accept a list of integers from the user
numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

# Use filter() with a lambda function to select only the even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Use map() with a lambda function to calculate the square of each even number
squared_even_numbers = list(map(lambda x: x ** 2, even_numbers))

# Display the final list
print("Squared even numbers:", squared_even_numbers)