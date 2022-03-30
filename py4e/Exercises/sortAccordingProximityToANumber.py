"""Customize Sort Function
You can also customize your own function by using the keyword argument key = function.
The function will return a number that will be used to sort the list (the lowest number first):
Example
Sort the list based on how close the number is to 50:"""
def proximityTo50(n):
    return abs(n - 50)

list = [100, 23, 50, 65, 83]

list.sort(key = proximityTo50)

print(list)

# Sorting is case sensitive. To make sure the array is sorted properly use lower or upper functions as the key
fruits = ["Banana", "peach", "Lemon", "apricot", "Watermelon"]
fruits.sort()
print(fruits) # This will print the fruits with capital letters first and then the words with lowercase letters.

fruits.sort(key = str.lower)
print(fruits)