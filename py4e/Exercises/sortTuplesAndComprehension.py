c = {"a": 10, "b": 1, "c": 22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
    
print(tmp)

tmp = sorted(tmp, reverse = True)
print(tmp)

################################################################
fhand = open("romeo.txt")
# dictionary to store words and counts
counts = dict()
# iterate over each line
for line in fhand:
    # create a list with the words of each line
    words = line.split()
    # get each word from the words list and set a key value pairs into counts dictionary.
    for word in words:
        # key = each word, value = the count of each signle word
        counts[word] = counts.get(word, 0) + 1
        
# list to store key value pairs        
lst = list()
# iterate over each key value pair in counts dictionary
for key, val in counts.items():
    # add the values in a new tupple with value pair order
    newtup = (val, key)
    # append the value of newtup to lst list
    lst.append(newtup)
    
# sort the value of the lst in reverse order    
lst = sorted(lst, reverse = True)

# print the first 10 value key pairs again in key value order
for val, key in lst[:10]:
    print(key, val)
    
############First Exercise with Comprehension####################
print(sorted([(v, k) for k,v in c.items()], reverse = True))
print(sorted([(v, k) for k, v in c.items()]))