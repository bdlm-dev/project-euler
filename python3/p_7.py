from math import ceil, sqrt
import util


"""
What is the 10001st prime number?
"""


class p_7(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = "7"

    def is_prime(self, number):
        sqrt_nr = ceil(sqrt(number))
        i = 2
        while i <= sqrt_nr:
            if not (number % i) and (i != number):
                return False
            i = self.incr(i)
        return True

    def incr(self, i):
        if i <= 2:
            return i + 1
        else:
            return i + 2

    def find_next_prime(self, prime):
        prime = self.incr(prime)
        while not self.is_prime(prime):
            prime = self.incr(prime)
        return prime

    def solve(self):
        i = 2
        prime = 3
        while i < 10001:
            prime = self.find_next_prime(prime)
            i = i + 1
        return prime


if __name__ == "__main__":
    instance = p_7()
    instance.run()
