import build_functions as bf

user_profile = bf.build_profile('Anas', 'Monjib',
	location='Finland',
	field='Computer science',
	university='University of Tampere',)

print(user_profile)

from build_functions import build_profile as bp

user_profile = bp('Anas', 'Monjib',
	location='Finland',
	field='Computer science',
	university='University of Tampere',)

print(user_profile)

from build_functions import *

user_profile = build_profile('Anas', 'Monjib',
	location='Finland',
	field='Computer science',
	university='University of Tampere',)

print(user_profile)
