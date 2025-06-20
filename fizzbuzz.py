def is_divisible_by(number: int, divisor: int) -> bool:
  return number % divisor == 0

def fizzbuzz(n: int) -> str:
  if is_divisible_by(n, 3) and is_divisible_by(n, 5):
    return "FizzBuzz"
  
  if is_divisible_by(n, 3):
    return "Fizz"
  
  if is_divisible_by(n, 5):
    return "Buzz"
  
  return str(n)
