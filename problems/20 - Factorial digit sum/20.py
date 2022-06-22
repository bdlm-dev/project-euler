factorial = 100
total = factorial
for i in range(factorial-1, 1, -1):
    total *= i
print(sum(int(j) for j in str(total)))
