#!C:/Python27
#Contact: nvanderende@gmail.com

"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
that the 6th prime is 13.

What is the 10 001st prime number?"""

#I hereby enscribe the Sieve of Eratosthenes

arbitrary_limit = 1000000 #I could do this a million times!
primes = [True] * arbitrary_limit #They're prime until they aren't.
numbers = []
for x in xrange(arbitrary_limit):
	numbers.append(x)
primes[0] = primes[1] = False #We can't use these, obviously
dprimes = dict(zip(numbers, primes))
prime_count = 0

for key in dprimes:
	if dprimes[key] == True:
		prime_count +=1
		#All factors marked non-prime
		for x in xrange(2*key, arbitrary_limit, key):
			dprimes[x] = False
		if prime_count == 10001:
			print key
			break
		else:
			continue
