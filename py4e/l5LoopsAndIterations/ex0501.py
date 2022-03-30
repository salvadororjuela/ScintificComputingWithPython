"""5.2 Write a program that repeatedly prompts a user for integer numbers until 
the user enters 'done'. Once 'done' is entered, print out the largest and smallest
of the numbers. If the user enters anything other than a valid number catch it with
a try/except and put out an appropriate message and ignore the number. Enter 7, 2, 
bob, 10, and 4 and match the output below."""

largest = None
smallest = None
while True:
    num = input("Enter an integer:")
    if num == "done":
        break
    try:
        maxnum = int(num)
        minnum = int(num)
        if largest is None:
            largest = maxnum
        if largest < maxnum:
            largest = maxnum
        if smallest is None:
            smallest = minnum
        if smallest > minnum:
            smallest = minnum
    except:
        print("Invalid input")
print(f"Maximum is {largest}")
print(f"Minimum is {smallest}")