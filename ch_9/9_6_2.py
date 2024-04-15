"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       Anas Monjib
Email:      amonjib@gmail.com
Student Id: H291936

"""


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


class IceCreamStand(Restaurant):
    """Simple attempt to represent an ice cream stand"""
    
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type,
                                            number_served)
        self.flavours = ["Vanilla", "Chocolate", "Strawberry", "Lime"]

    def describe_flavours(self):
        print("The flavours available are:")
        for flavour in self.flavours:
            print(" -" + flavour)
    

def main():
    restaurant_1 = Restaurant("Javeloni", "Italian", 10)
    restaurant_2 = Restaurant("Uncle Joe", "American", number_served=253)
    restaurant_3 = Restaurant("Akl Merracesh", "Moroccan")
    icecreamctand_1 = IceCreamStand("Ice", "Ice cream", number_served=13)

    print(restaurant_1.restaurant_name)
    print(restaurant_1.cuisine_type)
    restaurant_1.open_restaurant()
    restaurant_1.describe_restaurant()
    restaurant_2.describe_restaurant()
    restaurant_3.describe_restaurant()
    restaurant_3.set_number_served(100)
    restaurant_3.describe_restaurant()
    restaurant_3.increment_number_served(253)
    restaurant_3.describe_restaurant()
    icecreamctand_1.describe_restaurant()
    icecreamctand_1.describe_flavours()


if __name__ == "__main__":
    main()
