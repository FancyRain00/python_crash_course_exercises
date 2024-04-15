class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		"""Intializing my restaurants name and cuisine type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		"""describes my restaurant"""
		print("My restaurants name will be " + self.restaurant_name.title()
			+ " and it will be " + self.cuisine_type + " cuisine.")
	
	def open_restaurant(self):
		"""Opens thy restaurant"""
		print("The " + self.restaurant_name.title() + "is now open!")

my_restaurant = Restaurant("monjib kebab", "Moroccain")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

	
