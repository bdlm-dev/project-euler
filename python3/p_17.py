import util


"""
If all the numbers from 
1 to 1000 inclusive 
were written out in words, 
how many letters would be used?
"""


class p_17(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = "17"

    def solve(self):
        words = [util.number_to_word(i) for i in range(1, 1001)]
        out = "".join(words).replace(" ", "").replace("-", "")
        return len(out)


if __name__ == "__main__":
    instance = p_17()
    instance.run()
