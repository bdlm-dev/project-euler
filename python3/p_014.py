import util


"""
Which starting number, under one million,
produces the longest Collatz chain?
"""


class p_14(util.Problem):
    def __init__(self):
        super().__init__()
        self.problem_id = "14"

    # this is very inefficiet. takes 20 seconds to solve.
    def solve(self):
        maximum = 1000000
        max_chain, max_number = 0, 0
        chain_lengths = [0] * (maximum + 1)

        for i in range(1, maximum + 1):
            chain_num, chain, length = i, [], 0

            while chain_num != 1 and chain_num >= i:
                chain.append(chain_num)
                if chain_num % 2 == 0:
                    chain_num //= 2
                else:
                    chain_num = 3 * chain_num + 1
                length += 1

            for j, num in enumerate(chain):
                if num <= maximum:
                    total_length = length - j
                    chain_lengths[num] = total_length

            if length + chain_lengths[chain_num] > max_chain:
                max_chain = length + chain_lengths[chain_num]
                max_number = i

        return max_number


if __name__ == "__main__":
    instance = p_14()
    instance.run()

"""
Very Inefficient, takes ~20 seconds to compute.
Can be improved by caching the chain lengths for numbers as they are computed
Then using that to avoid repeated calculations
Improved version is ~20x faster, taking ~1s

for i in range(1, maximum + 1):
    chain_num, chain_len = i, 0
    while chain_num != 1:
        chain_len += 1
        if chain_num in chain_cache.keys():
            chain_len += chain_cache[chain_num]-1
            chain_num = 1
        if chain_num % 2:
            chain_num = (3 * chain_num) + 1
        else:
            chain_num /= 2
    chain_len += 1
    chain_cache[i] = chain_len
    if chain_len > max_chain:
        max_chain = chain_len
        max_number = i
"""