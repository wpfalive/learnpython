def scan(str):
	result = []
	directions = ('north', 'south', 'east', 'west', 'down', 'up', 'left','right', 'back')
	verbs = ('go', 'stop', 'kill', 'eat')
	stops = ('the', 'in', 'of', 'from', 'at', 'it')
	nouns = ('door', 'bear', 'princess', 'cabinet')
#	numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
	errors = 'error'
	words = str.split()
	for word in words:
		if word in directions:
			element = ('direction', word)
		elif word in verbs:
			element = ('verb', word)
		elif word in stops:
			element = ('stop', word)
		elif word in nouns:
			element = ('noun', word)
		elif convert_number(word): 
			element = ('number', convert_number(word))
		else:
			element = ('error', word)
		result.append(element) 	
	return result

def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None

