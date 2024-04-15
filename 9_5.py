class User():
	"""A simple user info and greeting."""
	def __init__(self, first_name, last_name, age, hobby):
		"""Intialize attributes to use later."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.hobby = hobby
		self.login_attempts = 0
	
	def describe_user(self):
		"""Later happend!:D Description of oneself"""
		print('\n' + self.first_name.title() + " " + 
			self.last_name.title() + " is " + str(self.age) + 
			" and their hobby is " + self.hobby + '.')
	
	def greet_user(self):
		"""Greeting from the great systematic response"""
		print("Welcome " + self.first_name.title() + " " + 
			self.last_name.title() +
			"! We hope you like your experience with us.")

	def increment_login_attempts(self):
		"""Increments the value of login_attempts by 1"""
		self.login_attempts += 1
		print(self.login_attempts)	# Just to check if method works

	def reset_login_attempts(self):
		"""Resets the value of login_attempts to 0"""
		self.login_attempts = 0
		print(self.login_attempts)	# Just to check if method works
		

me = User('anas', 'monjib', 20, 'coding')
user1 = User('aiamn', 'souri', 19, 'socializing')
user2 = User('danjar', 'ibrahimi', 21, 'reading')

me.describe_user()
me.greet_user()

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.reset_login_attempts()
user2.increment_login_attempts()