class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		"""Intializing my restaurants name and cuisine type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	
	def describe_restaurant(self):
		"""describes my restaurant"""
		print("My restaurants name will be " + self.restaurant_name.title()
			+ " and it will be " + self.cuisine_type + " cuisine.")
	
	def open_restaurant(self):
		"""Opens thy restaurant"""
		print("The " + self.restaurant_name.title() + "is now open!")
	
	def read_number(self):
		"""Printing the number of custumers served today"""
		print("-The number of people served is " + 
		str(self.number_served) + '.')
	
	def update_restaurant(self, number):
		"""
		Being able to modify value thourgh method
		Reject change if trying to roll back.
		"""
		if number >= self.number_served:
			self.number_served = number
		else:
			print("You can't roll back value!")
	
	def incriment_number(self, amount):
		"""Add todays amount to number served."""
		self.number_served += amount


my_restaurant = Restaurant("monjib kebab", "Moroccain")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.read_number()
my_restaurant.number_served = 5
my_restaurant.read_number()
my_restaurant.update_restaurant(20)
my_restaurant.read_number()
my_restaurant.incriment_number(50)
my_restaurant.read_number()
