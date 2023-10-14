import util


"""
Find the sum of all of the 
multiples of 3 or 5
below 1000
"""


class p_1(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = "1"

    def solve(self):
        return sum(i for i in range(1000) if not i % 3 or not i % 5)


if __name__ == "__main__":
    instance = p_1()
    instance.run()

