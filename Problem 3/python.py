#!C:/Python27
#Contact: nvanderende@gmail.com
import math

"""Taken from projecteuler.net/problems

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Taking the following approach: Starting with the first non-1 prime, check to
see if it's a factor. If it is, reassign to that value and check the new value
against the next integer value for factorization. This works because eventually
you work down to a factor of n which cannot be divided (i keeps increasing) and
then you hit the sqrt(n) upper bound, and you're done."""

number = 600851475143
def prime_factor(value):
	count = 2
	while count * count < value:
		while value % count ==0:
			value = value / count
		count += 1
	return value

solution = prime_factor(number)
print solution
