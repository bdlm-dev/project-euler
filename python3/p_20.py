import util


"""
Find the sum of the digits in the number 100!. 
"""


class p_20(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = "20"

    def solve(self):
        factorial = 100
        total = factorial
        for i in range(factorial - 1, 1, -1):
            total *= i
        return sum(int(j) for j in str(total))


if __name__ == "__main__":
    instance = p_20()
    instance.run()
