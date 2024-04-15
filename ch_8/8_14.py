def car_info(brand, model, **more_info):
	"""First try. Good luck!"""
	car = {}
	car['brand']= brand
	car['model']= model
	for n, i in more_info.items():
		car[n]= i
	return car

car_i = car_info('Mercedes-Benz', 'Sedan',
	year= str(2020),
	color='black',)
print(car_i)
#For first try without looking at the example. Pretty good.
#The problem in these programs is that I never know what to comment on!
#Really sad for future me trying to figure out something from these :p
