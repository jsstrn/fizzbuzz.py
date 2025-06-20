import unittest
from fizzbuzz import fizzbuzz

class FizzBuzz(unittest.TestCase):
  def test_returns_fizz_when_divisible_by_3(self):
    self.assertEqual(fizzbuzz(6), "Fizz")
    self.assertEqual(fizzbuzz(9), "Fizz")
    self.assertEqual(fizzbuzz(12), "Fizz")
  
  def test_returns_buzz_when_divisible_by_5(self):
    self.assertEqual(fizzbuzz(10), "Buzz")
    self.assertEqual(fizzbuzz(20), "Buzz")
    self.assertEqual(fizzbuzz(25), "Buzz")
  
  def test_returns_fizzbuzz_when_divisible_by_3_and_5(self):
    self.assertEqual(fizzbuzz(30), "FizzBuzz")
    self.assertEqual(fizzbuzz(45), "FizzBuzz")
    self.assertEqual(fizzbuzz(60), "FizzBuzz")
  
  def test_returns_number_when_not_divisible_by_3_or_5(self):
    self.assertEqual(fizzbuzz(7), "7")
    self.assertEqual(fizzbuzz(8), "8")
    self.assertEqual(fizzbuzz(11), "11")
  
if __name__ == "__main__":
    unittest.main()
