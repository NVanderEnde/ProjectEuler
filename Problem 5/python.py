#!C:/Python27
#Contact: nvanderende@gmail.com

"""2520 is the smallest number that can be divided by each of the numbers from 
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?"""

#Brute force method:
#Start the count at 20 and increment in steps of 20 since 20 is the largest
#denominator, it must be the largest factor

count = 20
list = [ ]
for x in xrange(1, 21):
	list.append(x)

while 1:
	win = 0
	for x in list:
		if count % x == 0:
			if x == 20:
				print count, "succeeded"
				win = 1
			else:
				continue
		else:
			#print count, "failed."
			break
	if win == 1:
		break
	count += 20

#The more efficient method that makes use of factorial properties
#creates the number, rather than finding it, by recursively generating the 
#lowest common multiples for each successive number

def greatest_common_denominator(x,y): 
	return y and greatest_common_denominator(y, x % y) or x
def lowest_common_multiple(x,y): 
	return x * y / greatest_common_denominator(x, y)


value=1
for x in xrange(1, 21):
	value = lowest_common_multiple(value, x)

print value
