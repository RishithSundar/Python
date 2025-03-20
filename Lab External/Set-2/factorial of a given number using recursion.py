def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
num = int(input("Enter a non-negative integer: "))
result = factorial(num)
print("The factorial of", num, "is", result)
