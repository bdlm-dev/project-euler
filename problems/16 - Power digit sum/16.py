# Find  the sum of the digits of 2^1000

num, power = 2, 1000
print(sum(int(char) for char in str(num**power)))

# returns 1366
