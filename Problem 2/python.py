#!C:\Python27
#Contact: nvanderende@gmail.com

"""Taken from projecteuler.net/problems

By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms."""

class Solution:

	def __init__(self):
		"""The first two numbers of the sequence are hard-coded so that the
		Fibonacci function can generate the rest more elegantly."""
		
		self.list = [1,1]
		self.sum = 0

	def fibonacci(self,n):
		"""Creates the fibonacci sequence up to the number specified
		as a list: e.g Fibonacci(1) = [1], Fibonacci(4) = [1, 1, 2, 3]"""
		
		for x in xrange(1,n):
			"""This may look wrong - isn't it supposed to be Fn(x-1) + Fn(x-2) ?
			- but since the Fn is created at the end of the for loop, Fn(x) is the
			same as Fn(x-1) since our self.list[x] refers to the last value added to
			the list. It's moved by the new value for this x at the end."""
			
			value = self.list[x] + self.list[x-1]
			self.list.append(value)
		return self.list


	def brute_force(self):
		"""Goes through the Fibonacci sequence, checks each value to see if it's
		even, and if it is, add it to the sum."""
		
		for value in self.list:
			if value%2 == 0:
				self.sum += value
		return self.sum
		
shazam = Solution()
shazam.fibonacci(32) #The fibonacci numbers are > 4,000,000 after the 30th one
#I could have calculated this in the program itself but why bother?
value = shazam.brute_force()
print value