def doubleChar(word):
	doubled = ""
	for l in word:
		doubled = doubled + (l*2)
	return doubled


word = "string"
print(doubleChar(word))		
