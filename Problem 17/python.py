#C:/Python27
#Contact: nvanderende@gmail.com

"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then 
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 
"and" when writing out numbers is in compliance with British usage."""

#First we need a function which converts a number to its written English equivalent

def number_to_english(input):
	"""Takes a natural number and converts it to its english equivalent.
	e.g 1234 becomes 'one thousand two hundred and thirty four' 
	Python's string operations are really nice for slicing up and manipulating input,
	so we'll use that."""
	
	input = str(input)
	answer = ''
	
	
	digit_map = {
	"0": '',
	"1": "one",
	"2": "two",
	"3": "three",
	"4": "four",
	"5": "five",
	"6": "six",
	"7": "seven",
	"8": "eight",
	"9": "nine"
	}
	
	#For these special cases, we'll grab the next number and use it to determine
	#Which 'teen' gets used
	teens_map = {
	"0": "ten",
	"1": "eleven",
	"2": "twelve",
	"3": "thirteen",
	"4": "fourteen",
	"5": "fifteen",
	"6": "sixteen",
	"7": "seventeen",
	"8": "eighteen",
	"9": "nineteen"
	}
	
	tens_map = {
	"0": "",
	"1": "ten",
	"2": "twenty",
	"3": "thirty",
	"4": "forty",
	"5": "fifty",
	"6": "sixty",
	"7": "seventy",
	"8": "eighty",
	"9": "ninety"
	}
	
	#We only need to go up to 1000, so no need for any higher places. 
	#These keys are ints because they're determined arithmetically, not taken from the input
	place_map = {
	0: '',
	1: "hundred",
	2: "thousand",
	}
	
	numdigits = len(input)
	show_place = 0
	if numdigits > 3: show_place = 1 #This ensures that even if we have a number like '11567'
									 #That it will print out the place value for 11 thousand
	skip_next = 0 #For the 'teen' special cases - we don't want to print, say, twelve two.
	
	for x, number in enumerate(input): #Starts from the 'front' of the number and works backwards
		if skip_next: 
			skip_next = 0
			continue #Skips to the next iteration of the loop. Continue is not pass
			
		digit = numdigits - x 
		if digit % 3 == 0: #A hundreds place
			answer += (digit_map[number] + ' ')
			show_place = 1
			
		if digit % 3 == 2: #A tens place
			if digit == 2 and input[x+1] != '0': answer += 'and ' 
			if number == '1': #A teen, so we skip the ones place
				answer += (teens_map[str(input[x+1])] + ' ')
				skip_next = 1
			else: answer += (tens_map[number] + ' ')
			
		if digit % 3 == 1: #A ones place
			answer += (digit_map[number] + ' ')
			show_place == 1
			
		if show_place: 	
			place = digit / 3 
			if digit % 3 != 0: place += 1
			#e.g one hundred million
			if digit > 3 and digit % 3 == 0: answer += (place_map[1] + ' ')
			if number != '0': answer += (place_map[place] + ' ')
			show_place = 0
		
	return answer
	
#So now we just loop through the range specified, strip the spaces per request, and we're done.

solution = ''
for x in xrange(1, 1001):
	solution += number_to_english(x)
print len(solution.replace(' ', ''))
