import util
from math import sqrt


"""
What is the value of the first triangle number 
to have over five hundred divisors?
"""


class p_12(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = "12"

    def solve(self):
        max_factors = 0
        nth_term = 0  # nth triangle number

        while max_factors < 500:
            factors = 0

            triangle_number = int(nth_term * (nth_term + 1) / 2)

            for j in range(1, round(sqrt(triangle_number))):
                if not (triangle_number % j):
                    factors += 2

            if factors > max_factors:
                max_factors = factors

            nth_term += 1

        return triangle_number


if __name__ == "__main__":
    instance = p_12()
    instance.run()
