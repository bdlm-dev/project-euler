# Find the sum of all primes below 2 million

def gen_primes(n):
    numbers = set(range(n, 1, -1))  # generates range & turns it into a set object
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes


print(sum(gen_primes(2000000)))

# returns 142913828922
