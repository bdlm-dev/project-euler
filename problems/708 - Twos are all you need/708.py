#  https://projecteuler.net/problem=708

#  Factorise positive integer n into prime factors
#  Define f(n) to be the product when each prime factor is replaced by 2

def f(n):
    i, j = 2, 0
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n /= i
            j += 1
    if n > 1:
        j += 1
    return 2 ** j


def s(N):
    total = 0
    for i in range(1, N):
        total += f(i)
        print(total)
    return total


print(s(10**8))


#  this works, but would require 250 hours runtime on this machine to get the correct answer.
