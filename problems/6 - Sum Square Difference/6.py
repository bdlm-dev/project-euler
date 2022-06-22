# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

squares = []
total = []

def sqr():
    i = 1

    while True:
        yield i * i, i
        i += 1


for num, j in sqr():
    if j > 100:
        break
    squares.append(num)
    total.append(j)

uno = sum(squares)
dos = sum(total) ** 2

print(dos - uno)

# returns 25164150
