p_words = {'Loop': 'using for in to loop through defined orders',
		'Booleon': 'a statement with true or false as answer',
		'List': 'a list of names or things',
		'String': 'basically what the computer understands as text',
		'Dictionary': 'this right here is an exm. of a dictionary',
		'set': 'using set() only prints items once if they are the same',
		'pyhton': 'computer programming language',
		'print': 'This statement prints the output on the screen',
		}

print("Python glossary:\n")

for term, meaning in p_words.items():
	print(term + ': ' + meaning)
