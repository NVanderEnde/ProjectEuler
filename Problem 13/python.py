#C:/Python27 
#Contact: nvanderende@gmail.com

""" Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

{omitted}"""

#This was delivered as one 5,000 digit number so I will not reproduce it here. I'll read it in from
#another file, instead.

number = open("number.txt", "r")
numbers = []

for row in number:
	#Trim the newlines and keep each 50 digit number as an entry in the list
	numbers.append(row.rstrip("\n"))

#Now, actually summing all 100 numbers as-is would be both a.) expensive and b.) silly, since
#the vast majority of those digits are so small that they are irrelevant. 9 digits should be enough
#but additional digits will ensure greater accuracy. Leaving all the digits still completes
#instantaneously on my machine.

for x, number in enumerate(numbers):
	#numbers[x] = int(number) / (10 ** 41)
	numbers[x] = int(number)

#Now we just sum these up.
solution = 0
for number in numbers:
	solution += number

#And make sure that we only keep the first ten digits
difference = len(str(solution)) - 10
if difference > 0:
	solution = solution / (10 ** difference)
	
print solution
