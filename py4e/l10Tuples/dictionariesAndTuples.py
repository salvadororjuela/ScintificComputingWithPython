# items() method
d = {"a": 10, "b": 1, "c": 22}
t = list(d.items())
print(t)

# Sort the new list of tuples
t.sort()
print(t)

# Traversing keys and values of a dictionary
"""This loop has two iterations varialbles because items returns a list of tuples and key,
val as a tuple assignment that successively iterates throujg each of the key-value pairs 
in the dictionary. This way does not sort"""
for key, val in list(d.items()):
    print(val, key)

# Traversing keys and values of a dictionary sorted
"""To do this, we first make a list of tuples where each tuple is (value, key). The
items method would give us a list of (key, value) tuples, but this time we want
to sort by value, not key. Once we have constructed the list with the value-key
tuple, is is a simple matter to sort the list in reverse order an print out the new,
sorted list"""

l = list()
for key, val in d.items():
    l.append((val, key))
l.sort(reverse=True)
print(l)

"""The following part demonstrate how to use this technique in a most complex example"""
import string
fhand = open("romeo-full.txt")
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans("", "", string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)
# Print the first 10 key-value pairs
for key, val in lst[:10]:
    print(key, val)