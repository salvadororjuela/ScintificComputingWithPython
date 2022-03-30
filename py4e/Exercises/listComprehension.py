fruits = ["Apple", "Banana", "Cherry", "Dates", "Guava", "Peach"]

fruitsWithE = [fruit for fruit in fruits if "e" in fruit]

fruitsWithoutApple = [fruit for fruit in fruits if fruit != "Apple"]

print(fruitsWithE)
print(fruitsWithoutApple)

# List with range()
newlist = [x for x in range(10)]
print(newlist)

# Same previous example but with a condition
newlist = [x for x in range(20) if x > 11]
print(newlist)

# Set the value of the new list to upper case
fruitsCapital = [fruit.upper() for fruit in fruits]
print(fruitsCapital)

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
# Example: Return "Orange" instead of "Banana"
"""The expression in the example below says:
"Return the item if it is not banana, if it is banana return orange"."""
noBanana = [fruit if fruit != "Banana" else "Orange" for fruit in fruits]
print(noBanana)
