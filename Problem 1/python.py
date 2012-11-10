#!C:\Python27
#Contact: nvanderende@gmail.com	
"""Taken from projecteuler.net/problems

Instructions: Add all the natural numbers below one thousand that are multiples
of 3 or 5."""


def brute_force(range):
	"""This is the brute force method - iterate over the range, check each 
	value to see if it matches with the requirements."""
	sum = 0

	for x in xrange(range):
		if x%3 == 0 or x%5 ==0:
			sum += x
		else:
			pass
	return sum
	
value = brute_force(1000)
print "Brute: ", value

def better_solution(range):
	"""So, wait - why do we bother to iterate over all the numbers in a range?
	We already know exactly what numbers we want - multiples of 3, and 5. Why
	not just generate sums of those numbers? Note that numbers which are
	multiples of both, meaning multiples of 15, will be counted twice so must
	be removed once."""
	#The count of 3 multiples in range, etc.
	#The 3 and 15 multiples need ranges +1 due to the way that Python's
	#xrange function iterates
	countlist = [ (range / 3) +1, (range / 5) , (range / 15) +1 ]
	sumlist = [0, 0, 0]
	integerlist = [3, 5, 15]
	
	for y in xrange(len(countlist)):
		for x in xrange(countlist[y]):
			sumlist[y] += integerlist[y] * x
	total = sumlist[0] + sumlist[1] - sumlist [2]
	return total
	
value = better_solution(1000)
print "Better: ", value
