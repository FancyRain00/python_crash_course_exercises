f_numbers = {'Aiman': 7, 'Danjar': 10, 'Iljas': 7,}
print(f_numbers)

# Tried to do it in a neatly formatted form. Too much work
print("Aiman: " + str(f_numbers['Aiman']) + "\n"
	"Danjar: " + str(f_numbers['Danjar']) + "\n"
	"Iljas: " + str(f_numbers['Iljas'])
	)

#simplified the process by using for in. didn't think it would work:D
for f_number in f_numbers:
	print(f_number + ": "  + str(f_numbers[f_number]))
