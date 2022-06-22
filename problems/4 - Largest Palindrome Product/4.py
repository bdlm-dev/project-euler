#  Palindromic numbers read the same whether forwards / backwards
#  Find largest palindromic number from the product of two 3-digit numbers

highest = 0

def palindrome(total: str):
    reverse = "".join([total[char-1] for char in range(len(total), 0, -1)])
    if total == reverse:
        return True
    else:
        return False


for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        x = i * j
        if palindrome(str(x)):
            if x > highest:
                highest = x
print(highest)

# returns 906609