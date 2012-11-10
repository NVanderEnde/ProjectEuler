#!C:/Python27
#Contact: nvanderende@gmail.com
import math

"""The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
"""

#First, sum of the squares:

square_sum = 0
sum_squares = 0
for x in xrange(1,101):
	sum_squares += math.pow(x, 2)
	square_sum += x
square_sum = math.pow(square_sum, 2)

difference = square_sum - sum_squares
print difference