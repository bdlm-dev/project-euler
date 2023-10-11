import util


"""
Find the largest prime factor of a given number, n
n = 600851475143
"""


class p_3(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = "3"

    def solve(self):
        n = 600851475143
        return self.f(n)

    def f(self, n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
        return n


if __name__ == "__main__":
    instance = p_3()
    instance.run()
