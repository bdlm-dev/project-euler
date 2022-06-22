# Find smallest number evenly divisible by all integers below 21

divisible = False
i = 20

while not divisible:
    check = 0
    for j in range(20):
        if not (i % (j+1)):
            check += 1
    if check == 20:
        divisible = True
    else:
        i += 20

print(i)

# returns 232792560
