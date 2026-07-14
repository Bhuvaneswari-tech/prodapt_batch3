#Function to check whether a string is a palindrome

def is_palindrome(s):
    text = s.lower()  # Convert the string to lowercase for case-insensitive comparison
    return text == text[::-1]  # Check if the string is equal to its reverse

# Test the function
#user input
word = input("Enter a string: ")
if is_palindrome(word):
    print(f'"My {word}" is a palindrome.') #print(word+"is a palindrome")
else:
    print(f'"{word}" is not a palindrome.')
    
#maDAM