import util


"""
What is the index of the first term in the 
Fibonacci sequence to contain 1000 digits?
"""


class p_25(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = "25"

    def solve(self):
        f1, f2, i = 1, 1, 2
        while len(str(f2)) < 1000:
            temp = f2
            f2 = f2 + f1
            f1 = temp
            i += 1
        return i


if __name__ == "__main__":
    instance = p_25()
    instance.run()
