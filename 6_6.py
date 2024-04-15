targets = ['joeel', 'sarah', 'hersh', 'rashed', 'jen']

answers = {'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

for name in targets:
	if name in answers.keys():
		print("Thank you " + name.title() + " for participating!")
	elif name not in answers.keys():
		print("This is an invite to " + name.title() +
			" to participate in our poll.")
