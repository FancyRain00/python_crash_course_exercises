def show_magicians(magicians):
	"""printing magician names"""
	for magician in magicians:
		wlcm = "Applodes for the great " + magician + '!'
		print(wlcm)

magicians_names = ['Hoodini', 'Aladdin', 'Fernard']
show_magicians(magicians_names)
