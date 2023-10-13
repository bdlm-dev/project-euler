import util


"""
There exists exactly one Pythagorean triplet for which 
a + b + c = 1000
Find the product abc
"""


class p_9(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = "9"

    def solve(self):
        for a in range(1, 1000):
            for b in range(1, 1000):
                c = 1000 - a - b
                if (a ** 2 + b ** 2) == c ** 2:
                    return a * b * c


if __name__ == "__main__":
    instance = p_9()
    instance.run()
