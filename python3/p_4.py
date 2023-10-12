import util


"""
Find the largest palindrome made from 
the product of two 3-digit numbers.
"""


class p_4(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = "4"

    def solve(self):
        highest = -1
        for i in range(999, 100, -1):
            for j in range(999, 100, -1):
                x = i * j
                s = str(x)
                if s == "".join(list(reversed(s))):
                    if x > highest:
                        highest = x
        return highest


if __name__ == "__main__":
    instance = p_4()
    instance.run()
