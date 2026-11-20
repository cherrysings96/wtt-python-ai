# Write a Python program to:
# 1.	Create a file and write a sentence into it

# 2.	Read the file content

# 3.	Count the number of words in the file

# Example:
# File content: "Python is easy to learn"
# Output: Number of words = 5

# Step 1: Create a file and write a sentence into it
file_name = "example.txt"
sentence = "Python is easy to learn"
with open(file_name, 'w') as file:
    file.write(sentence)
# Step 2: Read the file content
with open(file_name, 'r') as file:
    content = file.read()
# Step 3: Count the number of words in the file
word_count = len(content.split())
print(f"File content: \"{content}\"")
print(f"Output: Number of words = {word_count}")
