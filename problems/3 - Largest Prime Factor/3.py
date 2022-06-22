# Find the largest prime factor of a given number

num = 600851475143

def f(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


print(f(num))

# returns 6857
