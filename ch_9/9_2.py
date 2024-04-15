class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		"""Intializing my restaurants name and cuisine type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		"""describes my restaurant"""
		print("\nThis restaurants name willl be " + self.restaurant_name.title()
			+ " and it wil be " + self.cuisine_type + " cuisine.")
	
	def open_restaurant(self):
		"""Opens thy restaurant"""
		print("The " + self.restaurant_name.title() + "is now open!")
	
my_restaurant = Restaurant("monjib kebab", "Moroccain")
your_restaurant = Restaurant("hallis kebab", "Turkish")
a_restaurant = Restaurant("j'aime le cheese", "French")

my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
a_restaurant.describe_restaurant()
