import util


"""
Find the difference between the sum of the 
squares of the first one hundred natural 
numbers and the square of the sum.
"""


class p_6(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = "6"

    @staticmethod
    def sqr():
        i = 1

        while True:
            yield i * i, i
            i += 1

    def solve(self):
        squares, total = [], []

        for num, j in self.sqr():
            if j > 100:
                break

            squares.append(num)
            total.append(j)

        return (sum(total) ** 2) - sum(squares)


if __name__ == "__main__":
    instance = p_6()
    instance.run()
