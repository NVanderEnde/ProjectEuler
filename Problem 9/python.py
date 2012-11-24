#C:/Python27
#Contact: nvanderende@gmail.com
import math

"""A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

We just solve for c and iterate through possible combinations of a, b, and c until
we find the answer.
"""


for a in xrange(500):
		for b in xrange (a, 500):
			c = math.sqrt(a**2 + b**2)
			if (a+b+c) == 1000:
				print a*b*c


