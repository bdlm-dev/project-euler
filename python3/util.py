import time
from math import floor, sqrt
from re import findall
from data import conj, number_dictionary, modifiers


class Problem:
    def __init__(self):
        self.problem_id = None

    def solve(self):
        pass

    def run(self):
        start = time.perf_counter_ns()
        answer = self.solve()
        end = time.perf_counter_ns()

        print(f"Problem {self.problem_id}\n - Returned: {answer}\n - Time Elapsed: {(end-start)/1000000:6f}ms")


# conveniently enough did this number -> words thing
# for a competition before, so was able to just patch it up
def digits_to_string(num: int, standalone=True):
    num = floor(num)
    string = ""
    if num == 0 and standalone:
        return "zero"
    if len(str(num)) == 3:
        string += number_dictionary[0][num // 100] + conj + "hundred" + \
                  ((bool(num - (num // 100) * 100)) * (conj + "and" + conj))
    num = int(str(num)[-2:])
    for length in range(len(str(num)) - 1, -1, -1):
        if length == 1 and num < 20:
            string += number_dictionary["exceptions"][int(str(num)[-1:])]
            break
        else:
            if length == 0 and str(num)[-1] == "0":
                break
            digit = int(str(num)[length - 1])
            string += number_dictionary[length][digit] + "-"

    return string.rstrip("-")


def parse_integer_value(n: int):
    # floor num to get only integer value, decimal string is calculated separately
    # converted to string then reversed with [::-1] so can be separated correctly
    num = str(floor(n))[::-1]
    # separate number into 3-digit bits using a regex in re.findall()
    bits = findall("..?.?", num)  # . means any character. ? means character could be missing
    # reverse each 3-digit bit so in correct order as reversed at the start
    # entire list doesn't need to be reversed, index can be used for scale modifier
    bits = [bit[::-1] for bit in bits]
    string = ""

    for index, bit in enumerate(bits):
        if index != 0:
            string = digits_to_string(int(bit)) + conj + modifiers[index * 3] + conj + string
        else:
            string = digits_to_string(int(bit), n < 1000)

    return string


def number_to_word(n: int):
    return parse_integer_value(n)


def get_factors(num):
    factors = [1]
    for i in range(2, int(round(sqrt(num)))):
        if not(num % i):
            factors.append(i)
            factors.append(int(num/i))
    return factors
