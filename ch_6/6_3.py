p_words = {'Loop': 'using for in to loop through defined orders', 
	'Booleon': 'a statement with true or false as answer', 
	'List': 'a list of names or things', 
	'String': 'basically what the computer understands as text', 
	'Dictionary': 'this right here is an exm. of a dictionary',
	}
print(p_words.keys())

print("Python glossary:\n")

for p_word in p_words:
	print(p_word + ':' + p_words[p_word])
