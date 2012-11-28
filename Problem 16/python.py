#C:/Python27
#Contact: nvanderende@gmail.com

"""2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?"""

value = str(2**1000) #Python's string functions make this a cinch

solution = 0
for number in value:
	solution += int(number)
print solution
