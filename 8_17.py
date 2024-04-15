#This is the program 8_11.py used in this work
# The point is to styl ethis one as well as I can

def make_great(magicians, great_magicians):
	"""I have no idea how to do this using the same list?!"""
	while magicians:
		great = 'The Great ' + magicians.pop()
		great_magicians.append(great)

def show_great(great_magicians):
	"""printing the result"""
	for great_magician in great_magicians:
		print(great_magician)

magicians = ['Hoodini', 'Aladdin', 'Fernard']
great_magicians = []

make_great(magicians[:], great_magicians)
#We used [:] to keep the original magicians and now we will show
# the great magicians, wich after we will show that the original
# list is still intact.
show_great(great_magicians)
print(magicians)
