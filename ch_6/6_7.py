aiman = {'name': 'aiman', 'age': '19', 'origin': 'marocco',}
danjar = {'name': 'danjar', 'age': '20', 'origin': 'kurdistan',}
ismail = {'name': 'ismail', 'age': '18', 'origin': 'egypt',}

people =[aiman, danjar, ismail,]

print("people:")
for person in people:
	print()
	for k, v in person.items():
		print(k + ': ' + v.title())
