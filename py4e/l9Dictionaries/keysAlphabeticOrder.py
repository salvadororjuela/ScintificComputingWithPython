"""If you want to print the keys in alphabetical order, you first make a list
of the keys in the dictionary using the keys method, and then sort
that list and loop through the sorted list, looking up each key and
printin out key-value pairs in sorted order as follows."""

counts = {"chuck": 1, "annie": 42, "jan": 100}
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])

"""First you see the list of keys in unsorted order that we get from
keys method. Then we see the key-value pairs in order from the for loop"""
