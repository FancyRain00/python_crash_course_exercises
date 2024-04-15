"""A Restaurant class that can be used as a module"""

class Restaurant:
    """Simple attempt to represent a restaurant"""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print("The restaurants name is", self.restaurant_name, "and the cousine"
              "type is", self.cuisine_type, "\nand it has served",
              self.number_served, "custumers.")

    def open_restaurant(self):
        print("The", self.restaurant_name, "restaurant is open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number
