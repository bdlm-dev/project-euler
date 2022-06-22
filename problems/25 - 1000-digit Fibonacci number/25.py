# Find the index of the first term in the Fibonacci sequence to contain 1000 digits

f1, f2, i = 1, 1, 2
while len(str(f2))<1000:
  temp = f2
  f2 = f2+f1
  f1 = temp
  i += 1
print(i)

# returns 4782