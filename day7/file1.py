# file = open('student.txt', 'r')
# data = file.read()
# print(data)
# file.close()

file = open('student.txt', 'a+')
file.write("This is a new line of text.\n")
file.write("This is another line of text.\n")
file.seek(0)  # Move the file pointer back to the beginning of the file
data = file.read()  # This will not read anything because the file pointer is at the end after writing
print(data)
file.close()

# file = open('student.txt', 'r')
# data = file.read()
# print(data)
# file.close()