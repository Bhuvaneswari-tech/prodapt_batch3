'''
Write a Python program to find the longest word in a sentence using a function.
Requirements:
Create a function named find_longest_word().
Accept a sentence from the user.
Split the sentence into words.
Find the word with the maximum length.
Return the longest word.
Display the result.

Expected Output 1
Enter a sentence: Python is an amazing programming language
Longest word: programming

'''

# Function to find the longest word
import time
def find_longest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

# User Input
text = input("Enter a sentence: ")

#start time
start_time = time.perf_counter() #high resolution timer better than time.time() for measuring short durations

# Function Call
result = find_longest_word(text)
print("Longest word:", result)

#end time
end_time = time.perf_counter()
#execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")

# #different approach
# # Function to find the longest word

# def find_longest_word(sentence):
#     return max(sentence.split(), key=len)

# # User Input
# text = input("Enter a sentence: ")

# # Function Call
# print("Longest word:", find_longest_word(text))