# find the sum of all the amicable numbers under 10000

def amicable_num(cap=10000):
  from math import sqrt
  
  def get_factors(num):
    factors = [1]
    for i in range(2,int(round(sqrt(num)))):
      if not(num%i):
        factors.append(i)
        factors.append(int(num/i))
    return sum(factors)
    
    
  amicable_numbers = []
  
  for i in range(1,cap):
    sum1 = get_factors(i)
    sum2 = get_factors(sum1)
    if sum1 == i:
      pass
    elif sum2 == i:
      amicable_numbers.append(sum1+sum2)
      
  print("The sum of the amicable numbers under %s is: " % cap)
  print(int(sum(amicable_numbers)/2))

# returns 31626