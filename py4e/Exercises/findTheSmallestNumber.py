smallest = None
numbers = [21, 23, 43, 53, 11, 68, 9, 75, 109]
for i in numbers:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
print(smallest)