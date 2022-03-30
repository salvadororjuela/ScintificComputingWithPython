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