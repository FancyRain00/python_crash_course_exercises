def make_great(magicians, great_magicians):
	"""adding 'The Great' to the magicians on a list"""
	for magician in magicians:
		wlcm = "The Great " + magician
		great_magicians.append(wlcm)

magicians_names = ['Hoodini', 'Aladdin', 'Fernard']
great_magicians = []

make_great(magicians_names, great_magicians)
print(great_magicians)

#This is probably the right way to do it though:->

def make_great(magicians, great_magicians):
	"""The right way to do it"""
	while magicians:
		great = 'The Great ' + magicians.pop()
		great_magicians.append(great)

def show_great(great_magicians):
	"""printing the result"""
	for great_magician in great_magicians:
		print(great_magician)


magicians = ['Hoodini', 'Aladdin', 'Fernard']
great_magicians = []

make_great(magicians, great_magicians)
show_great(great_magicians)
