import util


"""
Find the sum of all the numbers that can be 
written as the sum of fifth powers of their digits.
"""


class p_30(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = "30"

    def solve(self):
        nums = []
        # 1^n is not considered a sum, so start from 2
        for i in range(2, 1000000):
            a = str(i)
            total = sum([int(char) ** 5 for char in a])
            if total == i:
                nums.append(i)

        return sum(nums)


if __name__ == "__main__":
    instance = p_30()
    instance.run()
