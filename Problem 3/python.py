#!C:/Python27
#Contact: nvanderende@gmail.com

"""Taken from projecteuler.net/problems

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Taking the following approach: Starting with the first non-1 prime, check to
see if it's a factor. If it is, reassign to that value and check the new value
against the next integer value for factorization (in this case, 600851475143).
This works because eventually you work down to a factor of n which cannot be 
divided (i keeps increasing) and then you hit the sqrt(n) upper bound, and 
you're done.

Iterating through 600 billion values would take, ehh, a long time, as would
checking each iteration for factorization and prime-ness. This is considerably
more efficient."""

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
