"""Suppose that you have a list of words and you want to sorte them from
longest to shortest:

The first loop builds a list of tuples, where each tuple is a word preceded by its
length.
sort compares the first element, lenght, first, and only considers the secont element
to break ties. The keyword argument reverse=True tells sort to go in decreasing order.
The second loops traverses the list of tuples and builds a list of words in descendig
order of length. The four-character words are sorted in reverse alphabetical order,
so "what" appears before "soft" in the resulting list."""

txt = "but soft what light in yonder window breaks"
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

print(res)