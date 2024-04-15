users = ['Alex', 'Aiman', 'Admin', 'Danjar', 'Hersh', 'Rashed']

if users:
	for user in users:
		if user == 'Admin':
			print("Hello " + user + "! Would you like to see the report?")
		else:
			print("Hello " + user + "! tank you for logging in!")
else:
	print("We need more users, Sir!")
