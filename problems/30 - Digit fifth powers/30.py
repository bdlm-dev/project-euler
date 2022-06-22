# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits

nums = []
for i in range(1000000):
  a = str(i)
  total = sum([int(char)**5 for char in a])
  if total == i:
    nums.append(i)

print(nums)
print(sum(nums))

# returns 443839
