# Create list of 20 numbers
numbers = [5, 2, 7, 5, 9, 3, 5, 1, 8, 5,
           6, 4, 5, 2, 7, 5, 9, 3, 5, 1]

print("Original List:")
print(numbers)

# User input
num = int(input("Enter number to delete extra occurrences: "))

count = 0
new_list = []

for i in numbers:
    if i == num:
        count += 1
        if count == 1:
            new_list.append(i)   # Keep first occurrence
    else:
        new_list.append(i)

print("Updated List:")
print(new_list)