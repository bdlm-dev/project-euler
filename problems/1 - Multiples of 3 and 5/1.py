# sum of all multiples of 3 & 5 below 1000

numbers = []
for i in range(1000):
    if not i % 3 or not i % 5:
        numbers.append(i)
print(sum(numbers))

# returns 233168
