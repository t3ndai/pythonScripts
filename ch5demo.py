#!/usr/bin/env python3.4
def myFunction(num, stringA):
	"""This is a function to see if the fridge has a food. fridge has to be 
	a dictionary defined outside of the function.
	the food to be searched for is in the string wantedFood"""

	if type(num) == type(int):
		print(num + 2)
	elif type(stringA) == type(""):
		print(stringA)
	raise TypeError("No such type")



