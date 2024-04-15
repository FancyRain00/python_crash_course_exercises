current_users = ['Alex', 'Aiman', 'Admin', 'Danjar', 'Hersh', 'Rashed']
new_users = ['RasheD', 'Oskari', 'Iljas', 'AIMAN', 'ali']

for new_user in new_users:
	if new_user.title() in current_users:
		print("Choose a new username!")
	elif new_user.lower() in current_users:
		print("Choose a new username!")
	else:
		print("This username is availeble.")
