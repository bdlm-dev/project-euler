import util


"""
By considering the terms of the fibonacci sequence
whose values do not exceed 4 million, find the sum
of the even-valued terms
"""


class p_2(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = 2

    def solve(self):
        lim = 4000000
        fib = [1, 2]

        while fib[-1] < lim:
            fib.append(fib[-1] + fib[-2])
        fib.pop(-1)

        return sum(i for i in fib if not i % 2)


if __name__ == "__main__":
    instance = p_2()
    instance.run()
