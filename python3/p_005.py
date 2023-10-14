import util


"""
What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?
"""


class p_5(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = "5"

    def solve(self):
        i = 1
        for k in (range(1, 21)):
            if i % k > 0:
                for j in range(1, 21):
                    if (i * j) % k == 0:
                        i *= j
                        break
        return i


if __name__ == "__main__":
    instance = p_5()
    instance.run()
