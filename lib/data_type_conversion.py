# Convert data types
number_str = "123"
integer_num = int(number_str)
float_num = float(number_str)

# Create a list
fruits = ["apple", "banana", "cherry", "date"]

# Iterate through a list using a for loop
print("Fruits:")
for fruit in fruits:
    print(fruit)

# Manipulate lists
fruits.append("grape")  # Add an item to the end of the list
fruits.insert(1, "blueberry")  # Insert an item at a specific position
fruits.remove("cherry")  # Remove an item by value
popped_fruit = fruits.pop()  # Remove and return the last item
fruits.sort()  # Sort the list in alphabetical order
reversed_fruits = list(reversed(fruits))  # Reverse the list

# Print the modified list
print("\nModified Fruits:")
for fruit in fruits:
    print(fruit)

# Manipulate strings
sentence = "This is a sample sentence."
uppercase_sentence = sentence.upper()  # Convert to uppercase
lowercase_sentence = sentence.lower()  # Convert to lowercase
split_sentence = sentence.split()  # Split the sentence into words

# Print the modified string
print("\nModified Sentence:")
print("Uppercase:", uppercase_sentence)
print("Lowercase:", lowercase_sentence)
print("Split:", split_sentence)
