def is_divisible_by(number: int, divisor: int) -> bool:
  return number % divisor == 0

def fizzbuzz(n: int) -> str:
  value = ""
  
  if is_divisible_by(n, 3):
    value += "Fizz"
  
  if is_divisible_by(n, 5):
    value += "Buzz"
  
  return value or str(n)