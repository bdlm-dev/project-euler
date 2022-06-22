# sum of all even-valued terms in the fibonacci sequence below 4 million

fibonacci = [1, 2]
even = []

while fibonacci[-1] < 4000000:
    fibonacci.append(fibonacci[-2] + fibonacci[-1])
fibonacci.pop(-1)
for elem in range(len(fibonacci)):
    if not fibonacci[elem] % 2:
        even.append(fibonacci[elem])
print(sum(even))

# returns 4613732
