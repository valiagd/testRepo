def summation(a, b):
  total = 0
  for n in range(a, b+1):
    total += n
  return total

a = summation(1, 100)
print a
b=summation(1,200) 
print a+b
