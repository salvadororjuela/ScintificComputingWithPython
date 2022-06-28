"""Given a string, count how many times each letter appears.
This program uses the get method used in dictionaries.
The get method takes a key and a default value. If the key appears in the 
dictionary, get returns the corresponding value; otherwise it returns the 
default value."""

word = "brontosaurus"
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1
print(d)
