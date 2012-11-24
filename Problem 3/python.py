#!C:/Python27
#Contact: nvanderende@gmail.com
import math

"""Taken from projecteuler.net/problems

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Taking the following approach: Starting with the first non-1 prime, check to
see if it's a factor. If it is, reassign to that value and check the new value
against the next integer value for factorization (in this case, 600851475143).
Once a factor is found, we continually factor it into our value until we reach 
the point where it can be factored no more - thus, the greatest prime factor."""

number = 600851475143
def prime_factor(value):
	divisor = 2
	while divisor * divisor < value:
		if value % divisor ==0:
			value = value / divisor
		else:
			divisor += 1
	return value

solution = prime_factor(number)
print solution