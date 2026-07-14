# add = lambda x, y: x + y
# print(add(5, 3))  # Output: 8
import time

find_largest_word = lambda sentence: max(sentence.split(), key=len)
sentence = input("Enter a sentence: ")
#start time
start_time = time.perf_counter()
largest_word = find_largest_word(sentence)

#end time
end_time = time.perf_counter()

print("Largest word:", largest_word)
#execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")

