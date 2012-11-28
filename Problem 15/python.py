#C:/Python27
#Contact: nvanderende@gmail.com

"""Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the 
bottom right corner.


How many routes are there through a 20x20 grid?"""

from math import factorial

#Okay. In order to make a step towards our goal, we have to make two steps total.
#For example, if I wanted to go down, I have to go right as well.
#So for an m x n grid, we have to make some combination of m (horizontal) and n (vertical) steps in
#order to get from one corner to the opposite. So how many mn combinations do we have?
#Using the combination binomial coefficient we can write this selection as
#(x/y) where x = (n + m)! and y = n! * m! - the selection of unordered values from the grid set.

def grid_paths(x_dimension, y_dimension):
	return (factorial(x_dimension + y_dimension) / (factorial(x_dimension) * factorial(y_dimension)))
	
print grid_paths(20,20)