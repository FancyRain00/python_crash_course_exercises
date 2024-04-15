def make_sandwich(bread, sauce, *fillings,):
	"""making a sandwich using unlimited parameters"""
	print("\nMaking " + bread + " sandwich with " + sauce +
		"-sauce and these toppings:")
	for filling in fillings:
		print('- ' + filling)


make_sandwich('white', 'garlic', 'tuna', 'shrimp', 'pickle',
	'feta cheese')
make_sandwich('baguette', 'hot', 'chiken', 'cheese')
make_sandwich('toast', 'mayonnaise', 'grilled cheese',)
