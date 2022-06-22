from math import floor, log10
from re import findall
from decimal import Decimal
from data import number_dictionary, modifiers

conj = " "  # conjugation, so whether it's "one-hundred" or "one hundred" etc.


def digits_to_string(num):
    """
    Return a string of the word for the integer of a number 0-999\n
    583.26 => "five-hundred-and-eighty-three"
    """

    num = floor(num)
    string = ""
    if num == 0:
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


def decimal_to_string(num):
    """
    Return a string of the word for the decimals of a number:\n
    decimalToString(6.384) => "three-eight-four"
    """

    # finds length of decimal by splitting at the decimal point, so can round
    try:
        length = len(str(num).split(".")[1])
    except IndexError:
        return ""  # no decimal value for number

    # gets only the decimals of a number
    # could be implemented via length of floor(num) and slicing, but this seems more efficient
    num = num - floor(num)
    num = round(num, length)  # round removes python's errors in calculation

    # strip the "0." at the start
    try:
        num = str(num)[2:]
    except ValueError:
        return ""
        # value error indicates it's trying to turn a blank string into an integer in this case,
        # so we can just return nothing as that means there is no decimal to this number

    string = (conj + "point" + conj) * bool(num)

    for char in num:
        string += number_dictionary[0][int(char)] + conj

    return string[:-1]  # [:-1 ] to remove trailing "-", removes need for conditional


def parse_integer_value(num):
    """
    Returns a string of the word for the integer of any number below 10^100:\n
    172667.2386 => one hundred and seventy-two thousand six hundred and sixty-seven
    Float can be passed, decimal can be truncated with floor()
    """
    # floor num to get only integer value, decimal string is calculated separately
    # converted to string then reversed with [::-1] so can be separated correctly
    num = str(floor(num))[::-1]
    # separate number into 3-digit bits using a regex in re.findall()
    bits = findall("..?.?", num)  # . means any character, ? means character could be missing
    # reverse each 3-digit bit so in correct order as reversed at the start
    # entire list doesn't need to be reversed, index can be used for scale modifier
    bits = [bit[::-1] for bit in bits]
    string = ""

    for index, bit in enumerate(bits):
        if index != 0:
            string = digits_to_string(int(bit)) + conj + modifiers[index * 3] + conj + string
        else:
            string = digits_to_string(int(bit))

    return string


def number_to_words(num):
    """
    Return string of the 'word-representation' of a number, input must be a string:
    587.16 => "five hundred and eighty-seven point one six"
    Input must be a string, or python will round above certain number of significant figures
    """
    num = Decimal(num)
    # modifiers only goes up to 10^99, so max is 999x10^99, or 9x10^101
    if log10(num) >= 102:
        return "Maximum input is x*10^101"
    string = ""
    string += parse_integer_value(num)
    string += decimal_to_string(num)
    return string
