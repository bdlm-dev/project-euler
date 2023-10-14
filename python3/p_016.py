import util


"""
What is the sum of the digits of the number 2^1000?
"""


class p_16(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = "16"

    def solve(self):
        num, power = 2, 1000
        return sum(int(char) for char in str(num ** power))


if __name__ == "__main__":
    instance = p_16()
    instance.run()
