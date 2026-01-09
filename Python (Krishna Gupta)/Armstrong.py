def is_armstrong(n):
   """check if number is armstrong (3 digits)"""
   total = sum(int(d)**3 for d in str(n))
   return total == n
print("7. Armstrong:", is_armstrong(370))
