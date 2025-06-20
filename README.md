# How to solve FizzBuzz

## Problem

Write a program that prints the numbers from 1 to 100. For numbers divisible by three print “Fizz” instead of the number and for numbers divisible by five print “Buzz”. For numbers which are divisible by both three and five print “FizzBuzz”.

## Solution

There are many ways to solve FizzBuzz. In this exercise, I use Test Driven Development (TDD) to solve it.

Firstly, our tests reveal that it is much easier to assert on a single value rather than the entire output from 1 to 100. By writing tests we know that `fizzbuzz()` needs to be outside the loop as it is much easier to assert that `fizzbuzz(3)` should return the value `'Fizz'`. This is what we mean when we say the tests *drive* the development.

With our test cases in place, it is much easier to write code to get it from red (failing) to green (passing). It is also much safer for us to refactor the code to make it easier to extend in future. For example, we might be asked to expand the conditions to print "Bazz" if the number is divisible by 7. Keeping the code clean definitely makes it easier to do this.
