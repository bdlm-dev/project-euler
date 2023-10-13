import util


"""
Find the sum of all the primes below two million.
"""


def gen_primes(n):
    numbers = set(range(n, 1, -1))  # generates range & turns it into a set object
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes


class p_10(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = "10"

    def solve(self):
        return sum(gen_primes(2000000))


if __name__ == "__main__":
    instance = p_10()
    instance.run()
