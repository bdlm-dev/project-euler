# Find the number below one million which produces the longest collatz chain

maximum = 1000000
max_chain, max_number = 0, 0

for i in range(1, maximum+1):
    print(i)
    chain_num, chain = i, []
    while chain_num != 1:
        chain.append(int(chain_num))
        if chain_num % 2:
            chain_num = (3 * chain_num) + 1
        else:
            chain_num /= 2
    chain.append(1)
    if len(chain) > max_chain:
        max_chain = len(chain)
        max_number = i

print(max_chain, max_number)

# answer is 837799, with a chain length of 525
