#!C:/Python27
#Contact: nvanderende@gmail.com

"""Taken from projecteuler.net/problems

A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

#First, need to define a palindrome.

def is_palindrome(value):
	"""Cut the number in half, flip the second half, and compare. Returns
	true or false."""
	value = str(value)
	split = len(value) / 2
	front = value[:split]
	back = value[split:]
	back = back[::-1] #Flipped
	
	palindrome = (front == back)
	return palindrome
	
#Here's the brute force method

solution = 0
#Can't go below 100 or above 999 - start from the top and count down
#It's faster than starting from the bottom and going up
for count_1 in xrange(999, 100, -1): 
	for count_2 in xrange(count_1, 100, -1):
		value = count_1 * count_2
		if value > solution:
			palindrome = is_palindrome(value)
			if palindrome == True:
				solution = value

print solution
