#C:/Python27
#Contact: nvanderende@gmail.com

"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

#Another task for a prime sieve - calculate all the primes and add them up.

limit = 2000000
solution = 0

def prime_sieve(limit):
	primes = [True] * limit
	primes[0] = primes[1] = False
	
	for x, prime in enumerate(primes):
		if prime:
			yield x
			for y in xrange(2*x, limit, x):
				primes[y] = False
		else:
			pass

primes = prime_sieve(limit)
for number in primes:
	solution += number
print solution
