# Find the 10001st prime

def sieve(n):
    primes = []
    num = 2
    while len(primes) <= n:
        prime = True
        for i in range(2, round(0.5 + (num ** 0.5))):
            if num % i == 0:
                prime = False
        if prime:
            primes.append(num)
        num += 1
    return str(primes[-1])


print(sieve(10001))

# returns 104743- switched to range(2, num**0.5) instead of num / 2- significantly faster
