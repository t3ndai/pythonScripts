#!/usr/bin/env python3.4

class Fridge:
	"""This class implements a fridge where ingredients 
	can be added and removed individually, or in groups. 
	The fridge will retain a count of every ingredient added or removed,
	and will raise an error if a sufficient quantity of an ingredient 
	isn't presend.
	Methods:
	has(food_name[,quantity]) - checks if the string food_name is in the 
	fridge. Quantity will be set to 1 if you don't specify a number.
	has_various(foods) - checks if enough of every food in the dictionary 
	is in the fridge
	add_one(food_name) - adds a single foodName to the fridge
	add_many(food_dict) - adds a whole dictionary filled with food
	get_one(food_name) - takes out a single food_name from the fridge
	get_many(food_dict) - takes out a whole dictionary worth of food
	get_ingredients(food) - If passed an object that has the __ingredients__
	      method, get_many will invoke this to the list of ingredients.
	"""

	def __init__(self, items = {}):
		'''Optionally pass an initial dictionary of items'''
		if type(items) != type({}):
			raise TypeError("Fridge requires a dictionary but was given %s," 
				%type(items))
		self.items = items
		return 

	def _add_multi(self, food_name, quantity):
		if (not food_name in self.items):
			self.items[food_name] = 0
		self.items[food_name] = self.items[food_name] + quantity

	def add_one(self, food_name):
		if type(food_name) != type(""):
			raise TypeError("add_one requires a string, given a %s" %type(food_name))
		else:
			self._add_multi(food_name,1)
		return True

	def add_many(self, food_dict):
		if type(food_dict) != type({}):
			raise TypeError("add_many requires a dict, got a %s" %type(food_dict))

		for item in food_dict.keys():
			self._add_multi(item, food_dict[item])
		return 

	def has(self, food_name, quantity=1):
		return self.has_various({food_name:quantity})

	def has_various(self, foods):
		try:
			for food in foods.keys():
				if self.items[food] < foods[food]:
					return False
			return True
		except KeyError:
			return False

	def _get_multi(self, food_name, quantity):
		try:
			if (self.items[food_name] is None):
				return False

			if (quantity > self.items[food_name]):
				return False
			self.items[food_name] = self.items[food_name] - quantity
		except KeyError:
			return False
		return quantity 

	def get_one(self, food_name):
		if type(food_name) != type(""):
			raise TypeError("get_one requires a string, given a %s" %type(food_name))
		else:
			result = self._get_multi(food_name, 1)
		return result

	def get_many(self, food_dict):
		if self.has_various(food_dict):
			foods_removed = {}
			for item in food_dict.keys():
				foods_removed[item] = self._get_multi(item, food_dict[item])
			return foods_removed

	def get_ingredients(self, food):
		try:
			ingredients = self.get_many(food._ingredients_())
		except AttributeError:
			return False

		if ingredients != False:
			return ingredients

class Omelet:
	def __init__(self, kind="cheese"):
		self.set_kind(kind)
		return 

	def _ingredients_(self):
		return self.needed_ingredients

	def get_kind(self):
		return self.kind

	def set_kind(self,kind):
		possible_ingredients = self._known_kinds(kind)
		if possible_ingredients == False:
			return False
		else:
			self.kind = kind
			self.needed_ingredients = possible_ingredients

	def set_new_kind(self, name, ingredients):
		self.kind = name
		self.needed_ingredients = ingredients
		return 

	def _known_kinds(self, kind):
		if kind == 'cheese':
			return {'eggs': 2, 'milk':1, 'cheese':1}
		elif kind == 'mushroom':
			return {'eggs':2, 'milk': 1, 'cheese': 1, 'mushroom': 2}
		elif kind == 'onion':
			return {'eggs': 2, 'milk': 1, 'cheese':1, 'onion':1}
		else:
			return False

	def get_ingredients(self, fridge):
		self.from_fridge = fridge.get_ingredients(self)

	def mix(self):
		for ingredients in self.from_fridge.keys():
			print("Mixing %d %s for the %s omelet" % self.from_fridge[ingredients], %ingredients, %self.kind)

		self.mixed = True

	def make(self):
		if self.mixed == True:
			print("Cooking the %s omelet!" %self.kind)
			self.cooked = True 


