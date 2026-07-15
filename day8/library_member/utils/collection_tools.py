from collections import Counter

def most_borrowed(books):
    return Counter(books).most_common(1)
