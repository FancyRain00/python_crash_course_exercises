#equality and inquality
thousand = 1000
print("When you write 1000, Does it mean thousand?")
print(thousand == 1000)
print("\nWhen you write 10000, That doesn't mean thousand, right?")
print(10000 != thousand)

#tests for lower() function and if item is in/not in list
tv_shows = ['Friends', 'Legacies', 'Lucifer', 'Mr. Robot']
favorite_tv = 'Mr. Robot'
print("\nIs friends one of your favorite shows")
print("Friends" in tv_shows)
print("\nIs mr. robot your favorite show")
print(favorite_tv.lower() == 'mr. robot')
