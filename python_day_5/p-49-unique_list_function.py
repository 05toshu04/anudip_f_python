def unique_list(lst):

    unique = []

    for i in lst:
        if i not in unique:
            unique.append(i)

    return unique


numbers = [1,2,3,2,4,5,1,6]

print("Unique Elements:")
print(unique_list(numbers))