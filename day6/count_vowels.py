# Function to count vowels

def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for ch in text.lower():
        if ch in vowels:
            count += 1

    return count


# User Input
sentence = input("Enter a string: ")

# Function Call
result = count_vowels(sentence)

print("Number of vowels:", result)


# Function to count each vowel using a dictionary

def count_vowels(text):
    vowel_count = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }

    for ch in text.lower(): #Artificial Intelligence
        if ch in vowel_count:
            vowel_count[ch] += 1

    return vowel_count


# User Input
sentence = input("Enter a string: ") #Artificial Intelligence

# Function Call
result = count_vowels(sentence)

print("Vowel Count:")
for vowel, count in result.items():
    print(vowel, ":", count)