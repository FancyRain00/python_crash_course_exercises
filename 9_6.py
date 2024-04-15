class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Intializing my restaurants name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Intializing my restaurants name and cuisine type"""
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavours = ["Vanilla", "Chocolate", "Mint", "Strawberry"]

    def list_flavours(self):
        print("The Ice cream flavours are:")
        for flavour in self.flavours:
            print(flavour)


def main():
    stand = IceCreamStand("heavenly ice", "Ice cream", number_served=10)
    stand.describe_restaurant()
    stand.list_flavours()


if __name__ == "__main__":
    main()
