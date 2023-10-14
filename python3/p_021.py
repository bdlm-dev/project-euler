import util


"""
Evaluate the sum of all the amicable numbers under 10000.
"""


class p_21(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = "21"

    def solve(self):
        cap = 10000
        amicable_numbers = []

        for i in range(1, cap):
            sum1 = sum(util.get_factors(i))
            sum2 = sum(util.get_factors(sum1))
            if sum1 == i:
                pass
            elif sum2 == i:
                amicable_numbers.append(sum1 + sum2)

        # each amicable pair is added twice, so halve the sum
        return int(sum(amicable_numbers)/2)


if __name__ == "__main__":
    instance = p_21()
    instance.run()
