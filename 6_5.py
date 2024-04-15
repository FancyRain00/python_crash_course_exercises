rivers = {'nile': 'egypt', 'amazon river': 'brazil', 'yangtze': 'china',}

for r, c in rivers.items():
	print("The " + r.title() + " runs through " + c.title() + ".")

print("\nThese are the river names:")
for river in rivers.keys():
	print(river.title())

print("\nThese are the country names:")
for c in rivers.values():
	print(c.title())
