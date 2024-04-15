"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       Anas Monjib
Email:      amonjib@gmail.com
Student Id: H291936

"""
from random import randint
x = randint(1, 6)

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        x = randint(1, self.sides)
        print("Your die rolled: ", x)


def main():
    first_die = Die(6)
    second_die = Die(10)
    third_die = Die(20)

    print("First, the 6-sided die:")
    for i in range(0, 10):
        first_die.roll_die()

    print("\nSecond, the 10-sided die:")
    for i in range(0, 10):
        second_die.roll_die()

    print("\nThird, the 20-sided die:")
    for i in range(0, 10):
        third_die.roll_die()


if __name__ == "__main__":
    main()
