#from ex. 4.1
pizzas = ['ananas', 'yalopeno', 'kebab']
friend_pizzas = pizzas[:]

pizzas.append('chicken')
friend_pizzas.append('mayonnaize')

print("My favorite pizza toppings are:")
for pizza in pizzas:
	print(pizza)

print("\nMy friend's favorite pizza toppings are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)
