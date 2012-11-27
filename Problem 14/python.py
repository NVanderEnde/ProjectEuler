#C:/Python27
#Contact: nvanderende@gmail.com

"""The following iterative sequence is defined for the set of positive integers:

n = n/2 (n is even)
n = 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers 
finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""

#The naive solution is to build the chain function, and iterate through 1 million values, returning
#the largest one. This is very wasteful, though, since it's highly unlikely that values under, say,
#500,000 are going to return larger chains than ones up around 900,000. Here's an important
#realization: the chain steps are identical, so to speak, no matter where you start. Once you
#reach a pre-calculated number, such as 40 in the example above, we know exactly what numbers will
#follow: 20, 10, 5, 16, 8, 4, 2 and 1. So if we remember these steps in a fast-access structure
#like a hash map, for example, we can save considerable time over calculating them anew.

solution = 0, 0
hashmap = { 
1 : 1
}
def sequence_builder(hashmap, value):
	if not hashmap.get(value, 0):
		if value % 2 == 0:
			#1 + because the last step counts as a step, too, although it's not accounted for
			#automatically
			hashmap[value] = 1 + sequence_builder(hashmap, value / 2)
		else: 
			hashmap[value] = 1 + sequence_builder(hashmap, 3 * value + 1)
	return hashmap[value]

for x in xrange (1, 1000000):
	chain_count = sequence_builder(hashmap, x)
	if chain_count > solution [1]: solution = x, chain_count
print solution