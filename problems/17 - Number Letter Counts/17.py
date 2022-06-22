# Find how many letters used in writing integers below 1001 in words

from functions import number_to_words as numword

words = []
for i in range(1, 1001):
  print(i)
  words.append(numword(i))

string = "".join(words)
string = string.replace(" ", "")
string = string.replace("-", "")
print(len(string)-4)

# code repurposed from my competition project of roughly the same idea but more depth
# returns 21224
