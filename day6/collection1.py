#Used to count occurrences of elements

'''
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
'''

from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)

print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1}


